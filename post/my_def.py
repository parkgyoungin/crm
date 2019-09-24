from django.conf import settings
from post.models import RansomwarePost
from django.db.models import Q
from django.urls import reverse

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
    pk_list = request.session.get(model, None)
    page = 1
    if pk_list:
        idx = pk_list.index(id)
        page = (idx)//PAGE + 1

    return page

def get_objects_by_request(request, model, default_order):
    session = request.session
    page = 1
    if request.GET:
        if session.get(model.__name__):
            page = request.GET['page']
            if request.GET.get('is_detail'):
                # GET 요청이면서 세션이 있고, 디테일 접근일경우 모든오브젝트
                order_by = request.GET.get('order_by', default_order)
                objects = RansomwarePost.objects.filter(id__in=session[model.__name__]).order_by(order_by)
            else:
                # 필터링 데이터
                search_field = request.GET['search_field']
                order_by = request.GET['order_by']
                filter_option = request.GET['filter_option']
                relation = request.GET['relation']
                data1 = request.GET['search_data']
                data2 = request.GET['search_data2']
                prev_objects = model.objects.filter(id__in=session[model.__name__])
                if filter_option == '__range':
                        if data1 == 'all_date' and data2 == 'all_date':
                            command = 'prev_objects.order_by(order_by)'
                        else:
                            command = 'prev_objects.filter(%s%s = [data1,data2]).order_by(order_by)' %(search_field, filter_option)
                else:
                    first_q = eval('Q(%s%s = data1)'%(search_field, filter_option, ))
                    second_q = eval('Q(%s%s = data2)'%(search_field, filter_option, ))
                    command = 'prev_objects.filter(first_q %s second_q).order_by(order_by)'%relation
                print(request.GET)
                print('command : ',command)
                objects = eval(command)
        else:
            # GET 요청이면서 세션이 없는경우 : 모든오브젝트
            objects = model.objects.all().order_by(default_order)
    else:
        # GET 요청이 아닐경우
        objects = model.objects.all().order_by(default_order)

    session[model.__name__] = list(objects.values_list('id', flat=True))
    return objects, page

def config_page_uri(request, id, model, PAGE):
    page = get_page(request, id, model, PAGE)
    uri = request.session[settings.LIST_CONDITIONS_ID].get('uri', reverse("post:list",args=['ransomware_post']))
    try:
        idx = uri.index('&page=')
        uri = uri[:idx] + '&page=%s'%page
    except:
        pass
    return uri