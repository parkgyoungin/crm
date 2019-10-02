from django.shortcuts import render
from main.models import Company, User
from post.models import DetectionPattern

def check(request, model,field_name, ele_id):
    success = False
    verbose_name = eval("%s._meta.get_field('%s').verbose_name"%(model,field_name))
    confirm_data = ""
    if request.method == 'POST':
        confirm_data = request.POST['confirm_data']
        if not eval("%s.objects.filter(%s='%s')"%(model,field_name,confirm_data)):
            success = True
    content = {
        'verbose_name':verbose_name,
        'confirm_data':confirm_data,
        'success':success,
        'ele_id':ele_id,
    }
    return render(request, 'post/check/check.html', content)