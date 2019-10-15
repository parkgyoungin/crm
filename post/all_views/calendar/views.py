from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
import datetime, calendar
from post.models import Schedule, Attendance, Comment
from post.all_forms.calendar.forms import ScheduleForm, AttendanceForm
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q


@login_required
def writeSchedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            obj =form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse("post:list",args=['calendar']))
    else:
        form = ScheduleForm()
    return render(request, 'post/calendar/write.html', {'form':form})

@login_required
def writeAttendance(request):
    today = datetime.datetime.today()
    success = False
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES, label_suffix="")
        if form.is_valid():
            obj =form.save(commit=False)
            obj.user = request.user
            obj.save()
            success = today.strftime('%H:%M:%S')
    else:
        form = AttendanceForm(label_suffix="")
    return render(request, 'post/calendar/attendance_write.html', {'form':form, 'success':success})

@login_required
def updateSchedule(request, id):
    instance = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(('post:list'), args=['calendar']))
    else:
        form = ScheduleForm(instance=instance)
    return render(request, 'post/calendar/write.html', {'form':form})

@login_required
def updateAttendance(request, id):
    today = datetime.datetime.today()
    success = False
    instance = Attendance.objects.get(id=id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=instance, label_suffix="")
        if form.is_valid():
            form.save()
            success = today.strftime('%H:%M:%S')
    else:
        form = AttendanceForm(instance=instance, label_suffix="")
    return render(request, 'post/calendar/attendance_write.html', {'form':form, 'success':success})

def listCalendar(request):
    today = datetime.datetime.today()
    default_GET = '?year=%s&month=%s'%(today.year, today.month)

    if not request.GET:
        return set_default(default_GET)

    else:
        try:
            year = int(request.GET['year'])
            month = int(request.GET['month'])
            if month == 13:
                return set_default(('?year=%s&month=%s'%(year+1, 1)))
            if month == 0:
                return set_default(('?year=%s&month=%s'%(year-1, 12)))

        except:
            return set_default(default_GET)

        days = get_content_month(year,month)
        return render(request, 'post/calendar/list.html', {'days': days})

def detailSchedule(request, id):
    model = Schedule

    object = model.objects.get(id=id)
    comment = Comment.objects.filter(model_name=model.__name__, model_pk=id)

    content = {
        'object': object,
        'comment': comment,
    }
    return render(request, 'post/calendar/detail.html', content)


def set_default(default_GET):
    redirect = reverse('post:list', args=['calendar']) + default_GET
    return HttpResponseRedirect(redirect)

def get_content_month(year, month):
    cal = calendar.Calendar(firstweekday=6)
    days = cal.monthdayscalendar(year, month)
    new_days = []
    for week in days:
        cur_week = []
        for day in week:
            if not day:
                schedule = None
                attendancd = None
            else:
                date = datetime.date(year, month, day)
                Q1 = Q(start_date__lte=date)
                Q2 = Q(end_date__gte=date)
                print(Q1, Q2)
                schedule = Schedule.objects.filter(Q1 & Q2).order_by('start_date')
                attendancd = Attendance.objects.filter(attendance_date=date)

            content = {'day':day , 'schedule': schedule, 'attendance': attendancd}
            cur_week.append(content)

        new_days.append(cur_week)

    return new_days