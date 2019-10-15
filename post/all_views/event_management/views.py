from post.all_forms.company_record.forms import CompanyRecordForm
from post.all_forms.event_management.forms import DetectionPatternForm, IPSTuneForm
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.conf import settings
from post.models import DetectionPattern, CompanyRecord, Comment, IPSTune
from post.my_def import set_default, get_objects_by_request_ex, set_session, get_side_obj, config_page_uri, view
from choice.choices import get_choices
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

PAGE = settings.OBJECTS_IN_PAGE

@login_required
def writeDetectionpattern(request):
    subs = {
        'id_attack_class_0': get_choices('attack_class_sub1', defalut=False),
        'id_attack_class_1': get_choices('attack_class_sub2', defalut=False),
        'id_attack_class_2': get_choices('attack_class_sub3', defalut=False),
        'id_attack_class_3': get_choices('attack_class_sub4', defalut=False),
        'id_attack_class_4': [('기타','기타')],
    }
    if request.method == 'POST':
        form = DetectionPatternForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse("post:list",args=['detectionpattern']))
    else:
        form = DetectionPatternForm()
    return render(request, 'post/detectionpattern/write.html', {'form':form, 'subs':subs})

@login_required
def writeIpstune(request):
    if request.method == 'POST':
        form = IPSTuneForm(request.POST, request.FILES)
        if form.is_valid():
            ips_tune = form.save(commit=False)
            ips_tune.user = request.user
            ips_tune.save()

            return HttpResponseRedirect(reverse("post:list",args=['ipstune']))
    else:
        form = IPSTuneForm()
    return render(request, 'post/ipstune/write.html', {'form': form})

@login_required
def updateDetectionpattern(request, id):
    subs = {
        'id_attack_class_0': get_choices('attack_class_sub1', defalut=False),
        'id_attack_class_1': get_choices('attack_class_sub2', defalut=False),
        'id_attack_class_2': get_choices('attack_class_sub3', defalut=False),
        'id_attack_class_3': get_choices('attack_class_sub4', defalut=False),
        'id_attack_class_4': [('기타', '기타')],
    }
    instance = DetectionPattern.objects.get(id=id)
    if request.method == 'POST':
        form = DetectionPatternForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = DetectionPatternForm(instance=instance)
    return render(request, 'post/detectionpattern/write.html', {'form':form, 'subs':subs})

@login_required
def updateIpstune(request, id):
    instance = IPSTune.objects.get(id=id)
    if request.method == 'POST':
        form = IPSTuneForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = IPSTuneForm(instance=instance)
    return render(request, 'post/ipstune/write.html', {'form':form})

def listDetectionpattern(request):
    model = DetectionPattern
    default_GET = '?reverse=false&order_by=-created&search_field=pattern_name&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

    if not request.GET:
        return set_default(model, request, default_GET)

    result = get_objects_by_request_ex(request, model, default_GET)
    if result['success']:
        objects, page = result['data']
    else:
        print(result['error'])
        return set_default(model, request, default_GET)

    set_session(request,objects,model)
    total = len(objects)
    paginator = Paginator(objects, PAGE)

    try:
        objects = paginator.page(page)
    except:
        objects = paginator.page(1)

    content = {
        'objects':objects,
        'total':total,
    }
    return render(request, 'post/detectionpattern/list.html', content)

def listIpstune(request):
    model = IPSTune
    default_GET = '?reverse=false&order_by=-created&search_field=title&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

    if not request.GET:
        return set_default(model, request, default_GET)

    result = get_objects_by_request_ex(request, model, default_GET)
    if result['success']:
        objects, page = result['data']
    else:
        print(result['error'])
        return set_default(model, request, default_GET)

    set_session(request,objects,model)
    total = len(objects)
    paginator = Paginator(objects, PAGE)

    try:
        objects = paginator.page(page)
    except:
        objects = paginator.page(1)

    content = {
        'objects':objects,
        'total':total,
    }
    return render(request, 'post/ipstune/list.html', content)


def detailDetectionpattern(request, id):
    model = DetectionPattern

    object = model.objects.get(id=id)
    view(object)
    pre_obj, next_obj = get_side_obj(request, id, model=model.__name__)
    comment = Comment.objects.filter(model_name=model.__name__, model_pk=id)

    uri = reverse('post:list', args=[model.__name__])
    if request.session[settings.LIST_CONDITIONS_ID].get(model.__name__):
        uri = config_page_uri(request, id, model.__name__, PAGE)

    content = {
        'object':object,
        'pre_obj':pre_obj,
        'next_obj':next_obj,
        'comment':comment,
        'uri' : uri,
    }

    return render(request, 'post/detectionpattern/detail.html', content)

def detailIpstune(request, id):
    model = IPSTune

    object = model.objects.get(id=id)
    view(object)

    pre_obj, next_obj = get_side_obj(request, id, model=model.__name__)
    comment = Comment.objects.filter(model_name=model.__name__, model_pk=id)

    uri = reverse('post:list', args=[model.__name__])
    if request.session[settings.LIST_CONDITIONS_ID].get(model.__name__):
        uri = config_page_uri(request, id, model.__name__, PAGE)

    content = {
        'object':object,
        'pre_obj':pre_obj,
        'next_obj':next_obj,
        'comment':comment,
        'uri' : uri,
    }

    return render(request, 'post/ipstune/detail.html', content)


def exportDetectionpattern(request):
    import xlwt

    MODEL = DetectionPattern
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="detectionPattern.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('탐지패턴 분석')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    # header
    columns = [
        ('IPS 탐지 패턴명', 'pattern_name'),
        ('위험도', 'risk'),
        ('CVE', 'cve'),
        ('IPS룰 등록일', 'rule_regist_date.strftime("%Y-%m-%d")'),
        ('업무처리상태', 'process_state'),
        ('보안장비 분류', 'get_equipment_class()'),
        ('공격 분류', 'get_attack_class()'),
        ('공격 유형 선택', 'get_attack_type()'),
        ('대응 방안', 'countermeasures'),
    ]

    for col_num, (hearder, _) in enumerate(columns):
        ws.col(col_num).width = 256 * CELL_WIDTH
        ws.write(row_num, col_num, hearder, font_style)
    row_num += 1

    pk_list= request.session.get(MODEL.__name__)

    if pk_list:
        objects = MODEL.objects.filter(id__in=pk_list).order_by(ORDER_BY)
    else:
        objects = MODEL.objects.all().order_by(ORDER_BY)

    font_style.font.bold = False
    for object in objects:
        for col_num, (_, field) in enumerate(columns):
            data = eval('object.%s'%field)
            ws.write(row_num, col_num, data, font_style)
        row_num += 1

    wb.save(response)
    return response