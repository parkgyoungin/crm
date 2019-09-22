from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm
from post.models import RansomwarePost, Comment
from django.core.paginator import Paginator
from django.conf import settings
from post.my_def import get_side_obj, get_pk_list, get_page

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
        'order_by':request.session[settings.LIST_CONDITIONS_ID].get('order_by', '-send_date'),
        'page': get_page(request, id, 'RansomwarePost', PAGE),
        'search_field':request.session[settings.LIST_CONDITIONS_ID].get('search_field', 'company'),
        'search_data': request.session[settings.LIST_CONDITIONS_ID].get('search_data', ""),
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
    order_by = request.GET.get('order_by', '-send_date')
    page = int(request.GET.get('page', 1))
    search_field = request.GET.get('search_field', 'company')
    search_data = request.GET.get('search_data', '')

    #objects = RansomwarePost.objects.all().order_by(order_by)
    objects = eval('RansomwarePost.objects.filter(%s__icontains = search_data).order_by(order_by)'%(search_field))
    request.session[settings.LIST_CONDITIONS_ID] = {
        'model':'RansomwarePost',
        'order_by': order_by,
        'pk_list': get_pk_list(objects),
        'search_field': search_field,
        'search_data': search_data,
    }

    total = len(objects)
    paginator = Paginator(objects, PAGE)
    objects = paginator.page(page)

    content = {
        'objects':objects,
        'total':total,
    }
    return render(request, 'post/ransomware/list.html', content)





