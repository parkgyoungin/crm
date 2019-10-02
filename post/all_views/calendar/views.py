from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
import datetime, calendar

def listCalendar(request):
    today = datetime.datetime.today()
    default_GET = '?year=%s&month=%s'%(today.year, today.month)

    if not request.GET:
        return set_default(default_GET)

    else:
        try:
            year = int(request.GET['year'])
            month = int(request.GET['month'])
        except:
            return set_default(default_GET)

        cal = calendar.Calendar(firstweekday = 6) # 6: 시작요일 일요일
        days = cal.monthdayscalendar(year, month)
        return render(request, 'post/calendar/list.html', {'days': days})

def set_default(default_GET):
    redirect = reverse('post:list', args=['calendar']) + default_GET
    return HttpResponseRedirect(redirect)

def set_in_range(range, i):
    if i in range:
        return i
    else:
        raw = range[0]
        high = range[-1]
