from post.all_forms.company_record.forms import CompanyRecordForm
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.conf import settings
from post.models import CompanyRecord, Comment
from post.my_def import set_default, get_objects_by_request_ex, set_session, get_side_obj, config_page_uri, view
from django.core.paginator import Paginator

PAGE = settings.OBJECTS_IN_PAGE

def writeCompanyrecord(request):
    if request.method == 'POST':
        form = CompanyRecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse("post:list",args=['companyrecord']))
    else:
        form = CompanyRecordForm()
    return render(request, 'post/companyrecord/write.html', {'form':form})

def updateCompanyrecord(request, id):
    instance = CompanyRecord.objects.get(id=id)
    if request.method == 'POST':
        form = CompanyRecordForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = CompanyRecordForm(instance=instance)
    return render(request, 'post/companyrecord/write.html', {'form':form, 'object':instance})

def listCompanyrecord(request):
    model = CompanyRecord
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
    return render(request, 'post/companyrecord/list.html', content)


def detailCompanyrecord(request, id):
    model = CompanyRecord

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

    return render(request, 'post/companyrecord/detail.html', content)

def exportCompanyrecord(request):
    import xlwt

    MODEL = CompanyRecord
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="companyRecord.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('수혜기업 이력관리')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    #header
    columns = [
        ('수혜기업명', 'company.name'),
        ('업무구분', 'division'),
        ('처리방법', 'process_method'),
        ('접수발생일시', 'occurr_date.strftime("%Y-%m-%d %H:%M")'),
        ('업무처리상태', 'process_state'),
        ('사업자 유형', 'company.business_type'),
        ('(정)-이름', 'company.manager_m_name'),
        ('(정)-부서', 'company.manager_m_depart'),
        ('(정)-휴대폰', 'company.manager_m_phone'),
        ('(정)-회사전화', 'company.manager_m_cphone'),
        ('(정)-이메일', 'company.manager_m_email'),
        ('(부)-이름', 'company.manager_s_name'),
        ('(부)-부서', 'company.manager_s_depart'),
        ('(부)-휴대폰', 'company.manager_s_phone'),
        ('(부)-회사전화', 'company.manager_s_cphone'),
        ('(부)-이메일', 'company.manager_s_email'),
        ('(기타)-이름', 'manager_e_name'),
        ('(기타)-부서', 'manager_e_depart'),
        ('(기타)-휴대폰', 'manager_e_phone'),
        ('(기타)-회사전화', 'manager_e_cphone'),
        ('(기타)-이메일', 'manager_e_email'),
        ('제목', 'title'),
        ('세부내용', 'content'),
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


