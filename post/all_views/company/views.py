from main.models import Company, Security, Internal, Virus, Ransomware, SendEmail
from post.all_forms.company.forms import CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm, Install_AddressForm
from post.my_def import get_fomrs, get_instance_forms, get_objects_by_request, get_objects_by_request_ex, set_session, set_default, get_side_obj, config_page_uri, view, delete_object
from django.db.models import Max
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

PAGE = 5
#admin = SendEmail.objects.all()[0]

@login_required
def writeCompany(request):
    admin = SendEmail.objects.all()[0]
    Forms = [CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm]
    id_max = Company.objects.all().aggregate(Max('id'))['id__max']
    next_id = id_max + 1 if id_max else 1

    if request.method == 'POST':
        forms = get_fomrs(Forms, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            se = forms['se_form'].save()
            it = forms['in_form'].save()
            vi = forms['vi_form'].save()
            ra = forms['ra_form'].save()
            ad = forms['ad_form'].save()
            co = forms['co_form'].save(commit=False)
            co.security = se
            co.internal = it
            co.virus = vi
            co.ransomware = ra
            co.address = ad
            co.user = request.user
            model_update(co, get_update_list(forms['co_form']))
            co.save()

            FROM = (admin.email, admin.password)
            TO = co.manager_m_email
            send_joined_email(FROM, TO)


            return HttpResponseRedirect(reverse('post:list', args=['company']))
    else:
        forms = get_fomrs(Forms)
    forms.update({'next_id':next_id})
    return render(request, 'post/company/write.html', forms)



def updateCompany(request, pk):
    Forms = {
        'main': CompanyForm,
        'sub': [SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm]
    }
    if request.method == 'POST':
        forms = get_instance_forms(Forms, pk, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            for key,form in forms.items():
                if key == 'co_form':
                    co = form.save(commit=False)
                    model_update(co, get_update_list(form))
                form.save()
            return HttpResponseRedirect(reverse('post:detail', args=['company', pk]))
    else:
        forms = get_instance_forms(Forms, pk)
    return render(request, 'post/company/write.html', forms)

def listCompany(request):
    model = Company
    default_GET = '?reverse=false&order_by=-created&search_field=name&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

    if not request.GET:
        return set_default(model, request, default_GET)

    result = get_objects_by_request_ex(request, model, default_GET, relation_model='business_category')
    if result['success']:
        objects, page = result['data']
    else:
        return set_default(model, request, default_GET)

    set_session(request, objects, model)
    total = len(objects)
    paginator = Paginator(objects, PAGE)

    try:
        objects = paginator.page(page)
    except:
        objects = paginator.page(1)

    content = {
        'objects': objects,
        'total': total,
    }
    content.update(Company.get_state())

    return render(request, 'post/company/list.html', content)

def detailCompany(request, id):
    model = Company

    object = model.objects.get(id= id)
    view(object)
    security = object.security
    internal = object.internal
    virus = object.virus
    ransomware = object.ransomware

    pre_obj, next_obj = get_side_obj(request, id, model=model.__name__)

    uri = reverse('post:list', args=[model.__name__])
    if request.session[settings.LIST_CONDITIONS_ID].get(model.__name__):
        uri = config_page_uri(request, id, model.__name__, PAGE)

    content = {
        'object': object,
        'security': security,
        'internal': internal,
        'virus' : virus,
        'ransomware': ransomware,
        'pre_obj': pre_obj,
        'next_obj': next_obj,
        'uri': uri,
    }

    return render(request, 'post/company/detail.html', content)


def deleteCompany(request, id):
    delete_object(Company, id, cascade=['address', 'security', 'internal', 'virus', 'ransomware'])
    return HttpResponseRedirect(reverse('post:list', args=['company']))

def get_update_list(form):
    names = {
        'large_etc' : 'large_scale',
        'major_etc' : 'major_partner',
        'smart_etc' : 'smart_factory',
    }
    update = {

    }
    for name in names:
        etc = form.cleaned_data.get(name)
        select = form.cleaned_data.get(names[name])
        if etc and select == '직접입력(추가)':
            update[names[name]] = etc
    return update

def model_update(obj, dic):
    for key, val in dic.items():
        exec('obj.%s = "%s" '%(key, val))

def send_joined_email(strFrom, strTo):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage

    password = strFrom[1]
    strFrom = strFrom[0]

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '한국산업기술보호협회 [가입완료]'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    content = '''
    <pre>
    안녕하십니까....
    가입되었습니다
    <img src="cid:image1">

    상세내용
    생략-
    </pre>
    '''
    msgText = MIMEText(content, 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('statics/image/test.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(strFrom, password)

    s.sendmail(strFrom, strTo, msgRoot.as_string())

    s.quit()

def exportCompany(request):
    import xlwt
    from post.export_excel import company, security, internal, virus, ransomware, get_dict

    MODEL = Company
    SPACE = (' ' * 10,)
    CELL_WIDTH = 15
    ORDER_BY = request.GET.get('order_by', 'created')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="company.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('수혜기업현황')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    row_num = 0

    # header
    columns = [('고객기업정보',)] + [(kor['name'],eng,'company') for eng, kor in company.items()] + [SPACE]
    columns += [('보안관제',)] + [(kor['name'],eng,'security') for eng, kor in security.items()] + [SPACE]
    columns += [('내부정보',)] + [(kor['name'],eng,'internal') for eng, kor in internal.items()] + [SPACE]
    columns += [('악성코드',)] + [(kor['name'],eng,'virus') for eng, kor in virus.items()] + [SPACE]
    columns += [('랜섬웨어',)] + [(kor['name'],eng,'ransomware') for eng, kor in ransomware.items()] + [SPACE]
    for col_num in range(len(columns)):
        ws.col(col_num).width = 256 * CELL_WIDTH
        ws.write(row_num, col_num, columns[col_num][0], font_style)

    row_num += 1

    pk_list = request.session.get(MODEL.__name__)
    if pk_list:
        objects = MODEL.objects.filter(id__in = pk_list).order_by(ORDER_BY)
    else:
        objects = MODEL.objects.all()

    # body
    font_style.font.bold = False
    for object in objects:
        company = get_dict(object)
        security = get_dict(object.security)
        internal = get_dict(object.internal)
        virus = get_dict(object.virus)
        ransomware = get_dict(object.ransomware)

        for col_num, column in enumerate(columns):
            if len(column)<3:
                continue
            field = column[1]
            obj = column[2]
            data = eval('%s[field]["data"]'%obj)
            ws.write(row_num, col_num, data, font_style)
        row_num += 1

    wb.save(response)
    return response
