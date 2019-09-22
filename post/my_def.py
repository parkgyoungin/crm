from django.conf import settings
from post.models import RansomwarePost

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
        field_name = form.__name__[:-4].lower()
        instance = eval("main_instance.%s"%field_name)
        new_forms[key] = form(data=POST, files=FILES, instance=instance, prefix=form.get_prefix())
    return new_forms

def to_date_widget(fields):
    from django import forms
    for key, field in fields.items():
        if key[-4:] == 'date':
            fields[key].widget = forms.DateInput(attrs={'type': 'date'})


def get_pk_list(objects):
    pk_list = []
    for object in objects:
        pk_list.append(object.id)
    return pk_list

def get_side_obj(request, id, model):
    condition = request.session[settings.LIST_CONDITIONS_ID]
    left_obj = None
    right_obj = None
    if condition['model']==model:
        left_pk, right_pk = get_side_pk(condition['pk_list'],id)
        if left_pk:
            left_obj = eval('%s.objects.get(id=%s)'%(model,left_pk))
        if right_pk:
            right_obj = eval('%s.objects.get(id=%s)'%(model, right_pk))

    return left_obj, right_obj

def get_side_pk(pk_list, id):
    idx = pk_list.index(id)
    try:
        right_pk = pk_list[idx+1]
    except:
        right_pk = None

    if idx-1 > -1:
        left_pk = pk_list[idx-1]
    else:
        left_pk = None

    return left_pk, right_pk

def get_page(request, id, model, PAGE):
    codition = request.session[settings.LIST_CONDITIONS_ID]
    page = 1
    if codition['model'] == model:
        pk_list = codition['pk_list']
        idx = pk_list.index(id)
        page = (idx)//PAGE + 1

    return page