from django import forms
from .models import User
from django.contrib.auth import logout , login

class UserCreationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')

    class Meta:
        model = User
        fields =['userid', 'password', 'password_confirm','email', 'user_name', 'nickname']
        widgets = {
            'userid': forms.TextInput,
            'password':forms.PasswordInput,
            'nickname': forms.TextInput,
        }

    def clean_password_confirm(self):
        password_confirm = self.cleaned_data['password_confirm']
        if password_confirm != self.cleaned_data['password']:
            raise forms.ValidationError('비밀번호가 서로 다릅니다.')
        return password_confirm

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname):
            raise forms.ValidationError('사용중인 닉네임 입니다.')
        return nickname

    def clean_userid(self):
        userid = self.cleaned_data['userid']
        if User.objects.filter(userid=userid):
            raise forms.ValidationError('사용중인 아이디 입니다.')
        return userid

class CheckUseridForm(forms.Form):
    userid = forms.CharField(max_length=50, label='아이디')

    def clean_userid(self):
        userid = self.cleaned_data['userid']
        if User.objects.filter(userid=userid):
            raise forms.ValidationError('이미 사용중인 아이디 입니다.')
        return userid


class CheckNicknameForm(forms.Form):
    nickname = forms.CharField(max_length=50, label='닉네임')

    def clean_userid(self):
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(userid=nickname):
            raise forms.ValidationError('이미 사용중인 닉네임 입니다.')
        return nickname


class loginForm(forms.Form):
    userid = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']
        userid = self.cleaned_data['userid']
        try:
            user = User.objects.get(userid=userid)
        except:
            user = None

        if user and not user.check_password(password):
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        elif not user:
            raise forms.ValidationError('존재하지 않는 아이디입니다.')

        return password

    def login(self, request):
        userid = self.cleaned_data['userid']
        user = User.objects.get(userid=userid)
        login(request, user)
