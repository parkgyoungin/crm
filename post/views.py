from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm, CheckForm, DetectionPatternForm, CommentForm
from main.models import Company, Security, Internal, Virus, Ransomware
from .models import DetectionPat, Comment
from django.db.models import Max
from .my_def import get_fomrs,get_instance_forms



def write(request, model):
    model = model[0].upper() + model[1:]
    command = 'write%s(request)'%model
    return eval(command)

def update(request, model, pk):
    model = model[0].upper() + model[1:]
    command = 'update%s(request, %s)' %(model,pk)
    return eval(command)

def list(request, model):
    model = model[0].upper() + model[1:]
    command = 'list%s(request)' % model
    return eval(command)

def detail(request, model,pk):
    model = model[0].upper() + model[1:]
    command = 'detail%s(request, %s)' %(model,pk)
    return eval(command)



#https://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms
def writeCompany(request):
    Forms = [CompanyForm, SecurityForm, InternalForm, VirusForm, RansomwareForm,]
    id_max = Company.objects.all().aggregate(Max('id'))['id__max']
    id_next = id_max + 1 if id_max else 1

    if request.method == 'POST':
        forms = get_fomrs(Forms, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            se = forms['se_form'].save()
            it = forms['in_form'].save()
            vi = forms['vi_form'].save()
            ra = forms['ra_form'].save()
            co = forms['co_form'].save(commit=False)
            co.security = se
            co.internal = it
            co.virus = vi
            co.ransomware = ra
            co.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_fomrs(Forms)
    forms.update({'id_next':id_next})
    return render(request, 'post/company/write.html', forms)

def updateCompany(request, pk):
    Forms = {
        'main': CompanyForm,
        'sub': [SecurityForm, InternalForm, VirusForm, RansomwareForm]
    }
    if request.method == 'POST':
        forms = get_instance_forms(Forms, pk, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            for form in forms.values():
                form.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_instance_forms(Forms, pk)
    return render(request, 'post/company/write.html', forms)

def listCompany(request):
    beneficComs = Company.objects.all()
    return render(request, 'post/company/list.html', {'beneficComs':beneficComs})

def detailCompany(request,pk):
    beneficCom = Company.objects.get(pk=pk)
    return render(request, 'post/company/detail.html', {'beneficCom':beneficCom})

def writeDetectionPattern(request):
    if request.method == 'POST':
        form = DetectionPatternForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = DetectionPatternForm()
    return render(request, 'post/detectionPattern/write.html', {'form':form})

def detailDetectionPattern(request, pk):
    MODEL_NAME = 'detectionPat'
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.model_pk = pk
            comment.model_name = MODEL_NAME
            comment.save()
    else:
        form = CommentForm()

    model = DetectionPat.objects.get(pk=pk)
    comments = Comment.objects.filter(model_name=MODEL_NAME, model_id=pk)
    content ={
        'model':model,
        'comments':comments,
        'form':form,
    }
    return render(request, 'post/detectionPattern/detail.html', content)

def updateDetectionPattern(request, pk):
    instance = DetectionPat.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetectionPatternForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = DetectionPatternForm(instance=instance)
    return render(request, 'post/detectionPattern/write.html', {'form':form})

#랜섬웨어


def check(request, model,field_name, ele_id):
    success = False
    verbose_name = eval("%s._meta.get_field('%s').verbose_name"%(model,field_name))
    confirm_data = ""
    if request.method == 'POST':
        confirm_data = request.POST['confirm_data']
        if not eval("%s.objects.filter(%s=%s)"%(model,field_name,confirm_data)):
            success = True
    content = {
        'verbose_name':verbose_name,
        'confirm_data':confirm_data,
        'success':success,
        'ele_id':ele_id,
    }
    return render(request, 'post/check/check.html', content)



