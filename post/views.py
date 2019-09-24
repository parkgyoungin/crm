from post.all_views.company.views import writeCompany, listCompany, detailCompany, updateCompany

from post.all_views.check.views import check

from post.all_views.search.views import search

from post.all_views.notification_status.views import writeRansomware_post, detailRansomware_post, updateRansomware_post, listRansomware_post

from post.all_views.notification_status.views import writeOutflow, updateOutflow, listOutflow, detailOutflow


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

