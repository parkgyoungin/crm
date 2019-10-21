from django import forms
from .models import User, SendEmail
from django.contrib.auth import logout , login
from post.my_def import rule1

def get_available(field, *args, **kwargs):
    title = None
    if kwargs.get('instance'):
        title = eval("kwargs['instance'].%s"%field)
    elif args:
        title = args[0][field]
    return title

class UserCreationForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['userid'].widget.attrs['readonly'] = 'true'
        self.fields['nickname'].widget.attrs['readonly'] = 'true'

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

        for error in rule1(password_confirm).values():
            raise forms.ValidationError(error)

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

class UpdateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')

    def __init__(self, *args, **kwargs):
        self.user_nickname = get_available('nickname', *args, **kwargs)
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['nickname'].widget.attrs['onchange'] = 'change_check(this)'

    class Meta:
        model = User
        fields =['password', 'password_confirm', 'email', 'user_name', 'nickname']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_password_confirm(self):
        password_confirm = self.cleaned_data['password_confirm']
        if password_confirm != self.cleaned_data['password']:
            raise forms.ValidationError('비밀번호가 서로 다릅니다.')
        return password_confirm

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if User.objects.filter(nickname=nickname) and nickname != self.user_nickname:
            raise forms.ValidationError('사용중인 닉네임 입니다.')
        return nickname

    def save(self, commit=True):
        user = super(UpdateUserForm, self).save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()

class SendEmailForm(forms.ModelForm):
    class Meta:
        model = SendEmail
        fields = '__all__'


    #def save(self, commit=True):
    #    send_email = super(SendEmailForm, self).save(commit=False)
        #password = self.cleaned_data['password']
        #send_email.set_password(password)
    #    send_email.save()

