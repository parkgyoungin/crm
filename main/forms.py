from django import forms
from .models import User

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

