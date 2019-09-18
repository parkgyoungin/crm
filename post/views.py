from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import *
from main.models import *



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
    Forms = [TbBeneficcomForm, TbSecurityForm, TbInternalForm, TbVirusForm, TbRansomForm,]
    if request.method == 'POST':
        forms = get_fomrs(Forms, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            be = forms['be_form'].save()
            for form in forms.values():
                instance = form.save(commit=False)
                instance.beneficCom = be
                instance.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_fomrs(Forms)
    return render(request, 'post/company/writeTest.html', forms)

def updateCompany(request, pk):
    Forms = {
        'main': TbBeneficcomForm,
        'sub': [TbSecurityForm, TbInternalForm, TbVirusForm, TbRansomForm]
    }
    if request.method == 'POST':
        forms = get_instance_forms(Forms, pk, request.POST, request.FILES)
        if False not in {form.is_valid() for form in forms.values()}:
            for form in forms.values():
                form.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        forms = get_instance_forms(Forms, pk)
    return render(request, 'post/company/writeTest.html', forms)

def listCompany(request):
    beneficComs = TbBeneficcom.objects.all()
    return render(request, 'post/company/list.html', {'beneficComs':beneficComs})

def detailCompany(request,pk):
    beneficCom = TbBeneficcom.objects.get(pk=pk)
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

def check_bnumber(request):
    if request.method == 'POST':
        form = CheckBnumberForm(request.POST)
        if form.is_valid():
            return render(request, 'post/company/idCheck.html', {'form':form, 'success':True})
    else:
        form = CheckBnumberForm()
    return render(request, 'post/company/idCheck.html', {'form':form})

def check_ips(request):
    if request.method == 'POST':
        form = CheckIpsForm(request.POST)
        if form.is_valid():
            return render(request, 'post/detectionPattern/ipsCheck.html', {'form':form, 'success':True})
    else:
        form = CheckIpsForm()
    return render(request, 'post/detectionPattern/ipsCheck.html', {'form':form})


def get_fomrs(forms, POST=None, FILES=None):
    new_forms = {}
    for form in forms:
        key = form.get_prefix() + '_form'
        new_forms[key] = form(data=POST, files=FILES, prefix=form.get_prefix())
    return new_forms

def get_instance_forms(forms, pk, POST=None, FILES=None):
    new_forms = {}

    main_model = forms['main'].Meta.model

    main_instance = main_model.objects.get(pk=pk)

    key = forms['main'].get_prefix()+'_form'

    new_forms[key] = forms['main'](data=POST, files=FILES, instance=main_instance, prefix=forms['main'].get_prefix())

    for form in forms['sub']:
        key = form.get_prefix()+'_form'
        foreignKey = main_model.__name__[0].lower() + main_model.__name__[1:] + '_id'
        instance = eval("form.Meta.model.objects.get(%s=main_instance.pk)"%foreignKey)
        new_forms[key] = form(data=POST, files=FILES, instance=instance, prefix=form.get_prefix())
    return new_forms

