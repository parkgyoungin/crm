from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import UserCreationForm, CheckUseridForm, CheckNicknameForm

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