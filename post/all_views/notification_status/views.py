from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm, OutflowForm
from post.models import RansomwarePost, Comment, Outflow
from django.core.paginator import Paginator
from django.conf import settings
from post.my_def import get_side_obj, get_pk_list, get_page, get_objects_by_request, config_page_uri
from django.db.models import Q


PAGE = 5

def writeRansomware_post(request):
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list",args=['ransomware_post']))
    else:
        form = RansomwarePostForm()
    return render(request, 'post/ransomware/write.html', {'form':form})

def detailRansomware_post(request, id):
    object = RansomwarePost.objects.get(id=id)
    pre_obj, next_obj = get_side_obj(request, id, model='RansomwarePost')
    comment = Comment.objects.filter(model_name='Ransomware_post', model_pk=id)

    content = {
        'object':object,
        'pre_obj':pre_obj,
        'next_obj':next_obj,
        'comment':comment,
        'uri' : config_page_uri(request, id, 'RansomwarePost', PAGE)
    }
    return render(request, 'post/ransomware/detail.html', content)

def updateRansomware_post(request, id):
    instance = RansomwarePost.objects.get(id=id)
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('main:home')))
    else:
        form = RansomwarePostForm(instance=instance)
    return render(request, 'post/ransomware/write.html', {'form':form})

def listRansomware_post(request):
    default_order = 'send_date'
    objects, page = get_objects_by_request(request, RansomwarePost, default_order)
    request.session[settings.LIST_CONDITIONS_ID] = {
        'model': 'RansomwarePost',
        'pk_list': list(objects.values_list('id', flat=True)),
        'uri': request.build_absolute_uri(),
    }

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

def writeOutflow(request):
    if request.method == 'POST':
        form = OutflowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list", args=['ransomware_post']))
    else:
        form = OutflowForm()
    return render(request, 'post/ransomware/write.html', {'form': form})


