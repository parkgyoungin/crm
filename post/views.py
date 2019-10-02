from post.all_views.company.views import writeCompany, listCompany, detailCompany, updateCompany

from post.all_views.check.views import check

from post.all_views.search.views import search,select

from post.all_views.notification_status.views import writeRansomwarepost, detailRansomwarepost, updateRansomwarepost, listRansomwarepost

from post.all_views.notification_status.views import writeOutflow, updateOutflow, listOutflow, detailOutflow

from post.all_views.company_record.views import writeCompanyrecord, updateCompanyrecord, listCompanyrecord, detailCompanyrecord

from post.all_views.event_management.views import writeDetectionpattern, listDetectionpattern, updateDetectionpattern, detailDetectionpattern

from post.all_views.event_management.views import writeIpstune, listIpstune, detailIpstune, updateIpstune

from post.all_views.calendar.views import listCalendar


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

def delete(request, model,pk):
    model = model[0].upper() + model[1:]
    command = 'delete%s(request, %s)' %(model,pk)
    return eval(command)

