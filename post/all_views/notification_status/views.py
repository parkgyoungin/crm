from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm, OutflowForm
from post.models import RansomwarePost, Comment, Outflow
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
    session = request.session
    page = 1
    default_order = 'send_date'
    if request.GET:
        if session.get('RansomwarePost'):
            page = request.GET['page']
            if request.GET.get('is_detail'):
                # GET 요청이면서 세션이 있고, 디테일 접근일경우 모든오브젝트
                order_by = request.GET.get('order_by', default_order)
                objects = RansomwarePost.objects.filter(id__in=session['RansomwarePost']).order_by(order_by)
            else:
                # 필터링 데이터
                search_field = request.GET['search_field']
                search_data = request.GET['search_data']
                order_by = request.GET['order_by']
                prev_objects = RansomwarePost.objects.filter(id__in=session['RansomwarePost'])
                objects = eval('prev_objects.filter(%s__icontains = search_data).order_by(order_by)' % (search_field))
        else:
            # GET 요청이면서 세션이 없는경우 : 모든오브젝트
            objects = RansomwarePost.objects.all().order_by(default_order)
    else:
        # GET 요청이 아닐경우
        objects = RansomwarePost.objects.all().order_by(default_order)

    session['RansomwarePost'] = list(objects.values_list('id', flat=True))
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

def config_page_uri(request, id, model, PAGE):
    page = get_page(request, id, model, PAGE)
    uri = request.session[settings.LIST_CONDITIONS_ID].get('uri', reverse("post:list",args=['ransomware_post']))
    try:
        idx = uri.index('&page=')
        uri = uri[:idx] + '&page=%s'%page
    except:
        pass
    return uri