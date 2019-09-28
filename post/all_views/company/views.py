from main.models import Company, Security, Internal, Virus, Ransomware
from post.all_forms.company.forms import CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm, Install_AddressForm
from post.my_def import get_fomrs, get_instance_forms, get_objects_by_request, get_objects_by_request_ex, set_session, set_default, get_side_obj, config_page_uri
from django.db.models import Max
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.core.paginator import Paginator

PAGE = 5

def writeCompany(request):
    Forms = [CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm, Install_AddressForm]
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
            ia = forms['ia_form'].save()
            co = forms['co_form'].save(commit=False)
            co.security = se
            co.internal = it
            co.virus = vi
            co.ransomware = ra
            co.address = ad
            co.install_address = ia
            model_update(co, get_update_list(forms['co_form']))
            co.save()
            return HttpResponseRedirect(reverse('post:list', args=['company']))
    else:
        forms = get_fomrs(Forms)
    forms.update({'next_id':next_id})
    return render(request, 'post/company/write.html', forms)



def updateCompany(request, pk):
    Forms = {
        'main': CompanyForm,
        'sub': [SecurityForm, InternalForm, VirusForm, RansomwareForm, AddressForm, Install_AddressForm]
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