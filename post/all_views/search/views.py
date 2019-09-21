from django.shortcuts import render
from main.models import Company

def search(request, model, field_name):
    objects = None
    verbose_name = eval("%s._meta.get_field('%s').verbose_name" % (model, field_name))
    if request.method == 'POST':
        objects = eval('model.objects.filter(field_name = request.POST["search_data"])')
    content = {
        'objects':objects,
        'verbose_name':verbose_name
    }
    template_name = model[0].lower() + model[1:]
    return render(request, 'post/search/%s.html'%template_name, content)