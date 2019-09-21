from django.shortcuts import render, HttpResponseRedirect, reverse
from post.all_forms.notification_status.forms import RansomwarePostForm
from post.models import RansomwarePost

def writeRansomware_post(request):
    if request.method == 'POST':
        form = RansomwarePostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("main:home"))
    else:
        form = RansomwarePostForm()
    return render(request, 'post/ransomware/write.html', {'form':form})