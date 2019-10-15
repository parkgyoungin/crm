from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from post.models import Timetable, Notice, Takeover, Comment
from post.all_forms.administration.forms import TimetableForm, NoticeForm, TakeoverForm
from post.my_def import set_default, get_objects_by_request_ex, set_session, get_side_obj, config_page_uri, view
from django.core.paginator import Paginator
from django.conf import settings

PAGE = settings.OBJECTS_IN_PAGE

@login_required
def writeTimetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES)
        if form.is_valid():
            ips_tune = form.save(commit=False)
            ips_tune.user = request.user
            ips_tune.save()

            return HttpResponseRedirect(reverse("post:list",args=['timetable']))
    else:
        form = TimetableForm()
    return render(request, 'post/timetable/write.html', {'form': form})

@login_required
def writeNotice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            ips_tune = form.save(commit=False)
            ips_tune.user = request.user
            ips_tune.save()

            return HttpResponseRedirect(reverse("post:list",args=['notice']))
    else:
        form = NoticeForm()
    return render(request, 'post/notice/write.html', {'form': form})

@login_required
def writeTakeover(request):
    if request.method == 'POST':
        form = TakeoverForm(request.POST, request.FILES)
        if form.is_valid():
            ips_tune = form.save(commit=False)
            ips_tune.user = request.user
            ips_tune.save()

            return HttpResponseRedirect(reverse("post:list",args=['takeover']))
    else:
        form = TakeoverForm()
    return render(request, 'post/takeover/write.html', {'form': form})

@login_required
def updateTimetable(request, id):
    instance = Timetable.objects.get(id=id)
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list",args=['timetable']))
    else:
        form = TimetableForm(instance=instance)
    return render(request, 'post/timetable/write.html', {'form':form})

@login_required
def updateNotice(request, id):
    instance =Notice.objects.get(id=id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list",args=['notice']))
    else:
        form = NoticeForm(instance=instance)
    return render(request, 'post/notice/write.html', {'form':form})

@login_required
def updateTakeover(request, id):
    instance = Takeover.objects.get(id=id)
    if request.method == 'POST':
        form = TakeoverForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("post:list",args=['takeover']))
    else:
        form = TakeoverForm(instance=instance)
    return render(request, 'post/takeover/write.html', {'form':form})

def listTimetable(request):
    model = Timetable
    default_GET = '?reverse=false&order_by=-created&search_field=title&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

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
    return render(request, 'post/timetable/list.html', content)

def listNotice(request):
    model = Notice
    default_GET = '?reverse=false&order_by=-created&search_field=title&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

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
    return render(request, 'post/notice/list.html', content)

def listTakeover(request):
    model = Takeover
    default_GET = '?reverse=false&order_by=-created&search_field=title&filter_option=__icontains&search_data=&search_data2=&relation=%26&page=1'

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
    return render(request, 'post/takeover/list.html', content)

def detailTimetable(request, id):
    model = Timetable

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

    return render(request, 'post/timetable/detail.html', content)

def detailNotice(request, id):
    model = Notice

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

    return render(request, 'post/notice/detail.html', content)

def detailTakeover(request, id):
    model = Takeover

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

    return render(request, 'post/takeover/detail.html', content)