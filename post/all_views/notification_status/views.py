from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm, OutflowForm
from post.models import RansomwarePost, Comment, Outflow, Weekness
from django.core.paginator import Paginator
from django.conf import settings
from post.my_def import get_side_obj, get_pk_list, get_page, get_objects_by_request, get_objects_by_request_ex, config_page_uri, save_connected_model, set_default
from django.db.models import Q


PAGE = 5

def writeRansomwarepost(request):
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list",args=['ransomwarepost']))
    else:
        form = RansomwarePostForm()
    return render(request, 'post/ransomware/write.html', {'form':form})

def writeOutflow(request):
    if request.method == 'POST':
        form = OutflowForm(request.POST)
        if form.is_valid():
            outflow = form.save()
            save_connected_model(Weekness, outflow, form, 12, request)

            return HttpResponseRedirect(reverse("post:list", args=['outflow']))
    else:
        form = OutflowForm()
    return render(request, 'post/outflow/write.html', {'form': form})

def detailRansomwarepost(request, id):
    model = RansomwarePost

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

    return render(request, 'post/ransomware/detail.html', content)

def detailOutflow(request, id):
    model = Outflow

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

    return render(request, 'post/outflow/detail.html', content)

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
    return render(request, 'post/outflow/write.html', {'form':form, 'weekness':weekness})

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