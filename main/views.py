from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .forms import UserCreationForm, CheckUseridForm, CheckNicknameForm, loginForm, UpdateUserForm, SendEmailForm
from django.contrib.auth import logout as set_logout
from django.contrib.auth.decorators import login_required
from post.models import Attendance
from main.models import SendEmail
import datetime


def home(request):
    #get_data, DB완성시 수정요망
    count = {
        'security' : 2451,
        'information' : 2011,
        'virus' : 1521,
        'ransomware' : 412,
    }
    use_count = {
        'security': 2451,
        'information': 1512,
        'virus': 2121,
        'ransomware': 531,
    }
    content = {
        'count': count,
        'use_count': use_count,
    }

    return render(request, 'main/home.html', content)

def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, label_suffix="")
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserCreationForm(label_suffix="")
    return render(request, 'main/join.html', {'form':form})

def check_userid(request):
    if request.method == 'POST':
        form = CheckUseridForm(request.POST)
        if form.is_valid():
            return render(request, 'main/useridCheck.html', {'form': form, 'success':True})
    else:
        form = CheckUseridForm()

    return render(request, 'main/useridCheck.html', {'form': form})

def check_nickname(request):
    if request.method == 'POST':
        form = CheckNicknameForm(request.POST)
        if form.is_valid():
            return render(request, 'main/nicknameCheck.html', {'form': form, 'success':True})
    else:
        form = CheckNicknameForm()

    return render(request, 'main/nicknameCheck.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.login(request)
            if not Attendance.objects.filter(user=request.user, attendance_date=datetime.date.today()):
                Attendance(user=request.user).save()
            redirect = request.GET.get('next') or reverse('main:home')
            return HttpResponseRedirect(redirect)
    else:
        form = loginForm()

    return render(request, 'main/login.html', {'form': form})

@login_required
def logout(request):
    set_logout(request)
    redirect = request.GET.get('next') or reverse('main:home')
    return HttpResponseRedirect(redirect)

@login_required
def confirmPassword(request):
    result = ''
    if request.method == 'POST':
        user = request.user
        if user.check_password(request.POST['password']):
            return HttpResponseRedirect(reverse('main:update_user'))
        result = '비밀번호가 다릅니다.'
    return render(request, 'main/confirm_password.html', {'result':result})

@login_required
def updateUser(request):
    user = request.user

    if request.user.is_admin:
        try:
            send_email = SendEmail.objects.all()[0]
        except:
            send_email = None


        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user)
            ad_form = SendEmailForm(request.POST, instance=send_email, prefix='ad')
            if form.is_valid() and ad_form.is_valid():
                form.save()
                ad_form.save()
                return HttpResponseRedirect(reverse('main:home'))
        else:
            form = UpdateUserForm(instance=user)
            ad_form = SendEmailForm(instance=send_email, prefix='ad')
        return render(request, 'main/update_user.html', {'form': form, 'ad_form':ad_form})

    else:
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('main:home'))
        else:
            form = UpdateUserForm(instance=user)
        return render(request, 'main/update_user.html', {'form': form})