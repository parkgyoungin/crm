from django import forms
from post.my_def import to_date_widget
from main.models import Company, Security, Internal, Virus, Ransomware

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
        to_date_widget(self.fields)

    class Meta:
        model = Security
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'se'

class InternalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InternalForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = Internal
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'in'

class VirusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VirusForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = Virus
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'vi'

class RansomwareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RansomwareForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = Ransomware
        fields = '__all__'

    @staticmethod
    def get_prefix():
        return 'ra'