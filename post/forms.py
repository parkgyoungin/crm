from django import forms
from . import choices
from django_summernote.widgets import SummernoteWidget
from main.models import Company,Security,Internal,Virus,Ransomware
from .models import Comment,DetectionPat

duplicate_check_fields = {
    'business_n',
}
onchange_fields = {
    'large_scale',
    'major_partner',
    'closed_net',
    'defense_industry',
    'smart_factory',
}

disable_fields = {
    'large_scale',
    'major_partner',
    'closed_net',
    'defense_industry',
    'smart_factory',
    'large_etc',
    'major_etc',
    'closed_etc',
    'defense_etc',
    'smart_etc',
    'operation_etc',
}

attrs_configs = [
    {'fields': duplicate_check_fields, 'attrs': 'onchange', 'value': 'change_check(this)'},
    {'fields': onchange_fields, 'attrs': 'onchange', 'value': 'set_another(this)'},
    {'fields': disable_fields, 'attrs': 'disabled', 'value': 'true'},
]

def get_available(field, *args, **kwargs):
    title = None
    if kwargs.get('instance'):
        title = eval("kwargs['instance'].%s"%field)
    elif args:
        title = args[0][field]
    return title

#https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms
class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        im_state = get_available('im_state', *args, **kwargs)
        super(CompanyForm, self).__init__(*args, **kwargs)

        #위젯 attribute 수정
        for key, field in self.fields.items():
            for config in attrs_configs:
                if key in config['fields']:
                    self.fields[key].widget.attrs[config['attrs']] = config['value']
        self.fields['im_state'].widget = forms.HiddenInput()

        #im_state 초기 설정
        if im_state:
            self.fields['im_1'].initial = bool(int(im_state[0]))
            self.fields['im_2'].initial = bool(int(im_state[1]))
            self.fields['im_3'].initial = bool(int(im_state[2]))
            self.fields['im_4'].initial = bool(int(im_state[3]))

    im_1 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange':'change_data()'}))
    im_2 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange':'change_data()'}))
    im_3 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange':'change_data()'}))
    im_4 = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'onchange':'change_data()'}))

    class Meta:
        model = Company
        exclude = ('security', 'internal', 'virus', 'ransomware')

    @staticmethod
    def get_prefix():
        return 'co'


class SecurityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecurityForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key[-4:] == 'date':
                self.fields[key].widget = forms.DateInput(attrs={'type':'date'})

    class Meta:
        model = Security
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'se'

class InternalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InternalForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key[-4:] == 'date':
                self.fields[key].widget = forms.DateInput(attrs={'type':'date'})

    class Meta:
        model = Internal
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'in'

class VirusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VirusForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key[-4:] == 'date':
                self.fields[key].widget = forms.DateInput(attrs={'type':'date'})

    class Meta:
        model = Virus
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'vi'

class RansomwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RansomwareForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key[-4:] == 'date':
                self.fields[key].widget = forms.DateInput(attrs={'type':'date'})

    class Meta:
        model = Ransomware
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'ra'

class DetectionPatternForm(forms.ModelForm):
    pat_name_h = forms.CharField(widget=forms.HiddenInput)
    etc_equ_class = forms.CharField(max_length=50, required=False)
    etc_att_class = forms.CharField(max_length=50, required=False)
    etc_att_type = forms.CharField(max_length=50, required=False,)
    class Meta:
        model = DetectionPat
        fields = '__all__'
        widgets = {
            'risk':forms.Select(choices=choices.sample),
            'pro_state':forms.Select(choices=choices.sample),
            'equ_class':forms.HiddenInput,
            'att_class':forms.HiddenInput,
            'att_type':forms.Select(choices=choices.sample_etc),
            'pat_analysis':SummernoteWidget,
            'rule_rdate':forms.DateInput(attrs={'type': 'date'}),
            'rule_udate':forms.DateInput(attrs={'type': 'date'}),
        }

class CommentForm(forms.ModelForm):
    com_class = forms.ChoiceField(choices=choices.com_class, required=False)
    class Meta:
        model = Comment
        exclude = ('model_name','model_pk')

class CheckBnumberForm(forms.Form):
    bnumber = forms.CharField(max_length=100, label='사업자등록번호')

    def clean_bnumber(self):
        bnumber = self.cleaned_data['bnumber']
        if Company.objects.filter(bc_cu_bnumber=bnumber):
            raise forms.ValidationError(' "%s"는 이미 사용중인 사업자등록번호 입니다.'%bnumber)
        return bnumber

class CheckIpsForm(forms.Form):
    pat_name = forms.CharField(max_length=100, label='IPS 탐지 패턴명')

    def clean_ips(self):
        pat_name = self.cleaned_data['pat_name']
        if DetectionPat.objects.filter(pat_name=pat_name):
            raise forms.ValidationError(' "%s"는 이미 사용중인 사업자등록번호 입니다.'%pat_name)
        return pat_name

class CheckForm(forms.Form):
    saved_data = forms.CharField(max_length=100)
    confirm_data = forms.CharField(max_length=100)
