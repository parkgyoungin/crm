from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from post.all_forms.notification_status.forms import RansomwarePostForm, OutflowForm, SymptomForm
from post.models import RansomwarePost, Comment, Outflow, Weekness, Symptom, ResponseType
from django.core.paginator import Paginator
from django.conf import settings
from post.my_def import get_side_obj, get_pk_list, get_page, get_objects_by_request, get_objects_by_request_ex, config_page_uri, save_connected_model, set_default, view, delete_object
from django.db.models import Q
from django.contrib.auth.decorators import login_required


PAGE = 5

@login_required
def writeRansomwarepost(request):
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse("post:list",args=['ransomwarepost']))
    else:
        form = RansomwarePostForm()
    return render(request, 'post/ransomware/write.html', {'form':form})

def deleteRansomwarepost(request, id):
    delete_object(RansomwarePost, id)
    return HttpResponseRedirect(reverse('post:list', args=['ransomwarepost']))

@login_required
def writeOutflow(request):
    if request.method == 'POST':
        form = OutflowForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            save_connected_model(Weekness, obj, form, 12, request)

            return HttpResponseRedirect(reverse("post:list", args=['outflow']))
    else:
        form = OutflowForm()
    return render(request, 'post/outflow/write.html', {'form': form})

def deleteOutflow(request, id):
    delete_object(Outflow, id)
    return HttpResponseRedirect(reverse('post:list', args=['outflow']))

@login_required
def writeSymptom(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.user = request.user
            symptom.save()
            save_connected_model(ResponseType, symptom, form, 5, request, forignkey='symptom')
            return HttpResponseRedirect(reverse("post:list", args=['symptom']))
    else:
        form = SymptomForm()
    return render(request, 'post/symptom/write.html', {'form': form})

def deleteSymptom(request, id):
    delete_object(Symptom, id)
    return HttpResponseRedirect(reverse('post:list', args=['symptom']))

def detailRansomwarepost(request, id):
    model = RansomwarePost

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

    return render(request, 'post/ransomware/detail.html', content)

def detailOutflow(request, id):
    model = Outflow

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

    return render(request, 'post/outflow/detail.html', content)

def detailSymptom(request, id):
    model = Symptom

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

    return render(request, 'post/symptom/detail.html', content)

def updateRansomwarepost(request, id):
    instance = RansomwarePost.objects.get(id=id)
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = RansomwarePostForm(instance=instance)
    return render(request, 'post/ransomware/write.html', {'form':form})

def updateOutflow(request, id):
    instance = Outflow.objects.get(id=id)
    weekness = Weekness.objects.filter(outflow_id=id)
    if request.method == 'POST':
        form = OutflowForm(request.POST, instance=instance)
        if form.is_valid():
            outflow = form.save()
            weekness.delete()
            save_connected_model(Weekness, outflow, form, 12, request)
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = OutflowForm(instance=instance)
    return render(request, 'post/outflow/write.html', {'form':form, 'weekness':weekness, 'object':instance})

def updateSymptom(request, id):
    instance = Symptom.objects.get(id=id)
    response = ResponseType.objects.filter(symptom_id=id)
    if request.method == 'POST':
        form = SymptomForm(request.POST, instance=instance)
        if form.is_valid():
            symptom = form.save()
            response.delete()
            save_connected_model(ResponseType, symptom, form, 5, request, forignkey='symptom')
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = SymptomForm(instance=instance)
    return render(request, 'post/symptom/write.html', {'form':form, 'response':response, 'object':instance})

def listRansomwarepost(request):
    model = RansomwarePost
    default_GET = '?reverse=false&order_by=-created&search_field=company__name&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

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
    return render(request, 'post/ransomware/list.html', content)


def listOutflow(request):
    model = Outflow
    default_GET = '?reverse=false&order_by=-created&search_field=company__name&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

    if not request.GET:
        return set_default(model, request, default_GET)

    result = get_objects_by_request_ex(request, model, default_GET, relation_model='weekness')
    if result['success']:
        objects, page = result['data']
    else:
        print('error : ', result.get('error', '알수없음'))
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
    return render(request, 'post/outflow/list.html', content)


def listSymptom(request):
    model = Symptom
    default_GET = '?reverse=false&order_by=-created&search_field=company__name&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

    if not request.GET:
        return set_default(model, request, default_GET)

    result = get_objects_by_request_ex(request, model, default_GET, relation_model='response_type')
    if result['success']:
        objects, page = result['data']
    else:
        print('error : ', result.get('error', '알수없음'))
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
    return render(request, 'post/symptom/list.html', content)

#from post.all_views.notification_status.views import get_filter_list_by_conn_model
#from post.models import Outflow
#get_filter_list_by_conn_model('a', Outflow)



def set_session(request, objects, model):
    request.session[settings.LIST_CONDITIONS_ID] = {
        model.__name__: {
            'pk_list': list(objects.values_list('id', flat=True)),
            'uri': request.build_absolute_uri()
        }
    }

def exportSymptom(request):
    import xlwt

    MODEL = Symptom
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="symptom.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('이상징후')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    columns = [
        ('탐지날짜', 'detect_date.strftime("%Y-%m-%d")'),
        ('기업명', 'company.name'),
        ('제품명', 'get_product_name()'),
        ('탐지명', 'detect_name'),
        ('출발지', 'start_point'),
        ('목적지', 'end_point'),
        ('Dport', 'dport'),
        ('국가', 'country'),
        ('공격유형', 'attack_type'),
        ('방향성', 'direction'),
        ('대응유형', 'get_response_type()'),
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

def exportOutflow(request):
    import xlwt

    MODEL = Outflow
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="outflow.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('기술유출')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    columns = [
        ('기업명', 'company.name'),
        ('문서번호', 'document_n'),
        ('발송날짜', 'send_date.strftime("%Y-%m-%d")'),
        ('URL', 'url'),
        ('발견 취약점', 'get_weekness()'),
        ('처리상태', 'process_state'),
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

def exportRansomwarepost(request):
    import xlwt

    MODEL = RansomwarePost
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ransomwarepost.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('랜섬웨어')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    columns = [
        ('기업명', 'company.name'),
        ('문서번호', 'document_n'),
        ('발송날짜', 'send_date.strftime("%Y-%m-%d")'),
        ('에이전트명', 'agent_name'),
        ('에이전트IP', 'agent_ip'),
        ('탐지일', 'detect_date.strftime("%Y-%m-%d")'),
        ('대상경로', 'path'),
        ('회신유무', 'reply'),
        ('파일명', 'file_name'),
        ('처리상태', 'process_state')
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