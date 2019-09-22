from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm
from post.models import RansomwarePost, Comment
from django.core.paginator import Paginator

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
    comment = Comment.objects.filter(model_name='Ransomware_post', model_pk=id)
    return render(request, 'post/ransomware/detail.html', {'object':object, 'comment':comment})

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
    objects = RansomwarePost.objects.all().order_by(order_by)

    return render(request, 'post/ransomware/list.html', {'objects':objects})
