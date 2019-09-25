from main.models import Company, Security, Internal, Virus, Ransomware
from post.all_forms.company.forms import CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm
from post.my_def import get_fomrs, get_instance_forms, get_objects_by_request, get_objects_by_request_ex, set_session, set_default
from django.db.models import Max
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.core.paginator import Paginator

PAGE = 5

def writeCompany(request):
    Forms = [CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm,]
    id_max = Company.objects.all().aggregate(Max('id'))['id__max']
    id_next = id_max + 1 if id_max else 1

    if request.method == 'POST':
        forms = get_fomrs(Forms, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            se = forms['se_form'].save()
            it = forms['in_form'].save()
            vi = forms['vi_form'].save()
            ra = forms['ra_form'].save()
            co = forms['co_form'].save(commit=False)
            co.security = se
            co.internal = it
            co.virus = vi
            co.ransomware = ra
            co.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_fomrs(Forms)
    forms.update({'id_next':id_next})
    return render(request, 'post/company/write.html', forms)

def updateCompany(request, pk):
    Forms = {
        'main': CompanyForm,
        'sub': [SecurityForm, InternalForm, VirusForm, RansomwareForm]
    }
    if request.method == 'POST':
        forms = get_instance_forms(Forms, pk, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            for form in forms.values():
                form.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_instance_forms(Forms, pk)
    return render(request, 'post/company/write.html', forms)

def listCompany(request):
    model = Company
    default_GET = '?order_by=created&search_field=company&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

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
    return render(request, 'post/company/list.html', content)

def detailCompany(request,pk):
    beneficCom = Company.objects.get(pk=pk)
    return render(request, 'post/company/detail.html', {'beneficCom':beneficCom})