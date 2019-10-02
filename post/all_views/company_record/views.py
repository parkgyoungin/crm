from post.all_forms.company_record.forms import CompanyRecordForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.conf import settings
from post.models import CompanyRecord, Comment
from post.my_def import set_default, get_objects_by_request_ex, set_session, get_side_obj, config_page_uri
from django.core.paginator import Paginator

PAGE = settings.OBJECTS_IN_PAGE

def writeCompanyrecord(request):
    if request.method == 'POST':
        form = CompanyRecordForm(request.POST)
        if form.is_valid():
            form.save()
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