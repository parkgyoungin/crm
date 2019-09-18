from django import forms
from . import choices
from django_summernote.widgets import SummernoteWidget
from django.utils.safestring import mark_safe
from main.models import *
from .models import *

#https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms

class TbBeneficcomForm(forms.ModelForm):
    bc_cu_bnumber_h = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = TbBeneficcom
        fields = '__all__'
        widgets = {

            'bc_im_ransomware': forms.CheckboxInput,

            'bc_ss_security': forms.Select(choices=choices.serstate, attrs={'required':'true'} ),

            'bc_ss_internal': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'bc_ss_virus': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'bc_ss_ransomware': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'bc_cu_business': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'bc_cu_comclass': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'bc_cu_path': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'bc_op_lmove': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'bc_op_lpartner': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'bc_op_closure': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'bc_op_defense': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'bc_cu_bnumber': forms.TextInput(attrs={'onclick':'popup_idChk()'}),

            'bc_sdate': forms.DateInput(attrs={'type':'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'be'

class TbSecurityForm(forms.ModelForm):
    class Meta:
        model = TbSecurity
        exclude = ('beneficCom',)
        widgets = {
            # 'se_ipsrule':forms.TextInput,

            # 'se_syslog':forms.HiddenInput(),

            'se_icmp':forms.HiddenInput(),

            'se_snmp':forms.HiddenInput(),
            'se_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'se_ips': forms.HiddenInput(),
            'se_sdate': forms.DateInput(attrs={'type':'date'}),
            'se_cdate': forms.DateInput(attrs={'type':'date'}),
            'se_edate': forms.DateInput(attrs={'type': 'date'}),
            'se_tdate': forms.DateInput(attrs={'type': 'date'}),

        }

    @staticmethod
    def get_prefix():
        return 'se'

class TbInternalForm(forms.ModelForm):
    class Meta:
        model = TbInternal
        exclude = ('beneficCom',)
        widgets = {
            'in_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'in_cdate': forms.DateInput(attrs={'type': 'date'}),
            'in_tdate': forms.DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'in'

class TbVirusForm(forms.ModelForm):
    class Meta:
        model = TbVirus
        exclude = ('beneficCom',)
        widgets = {
            'vi_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'vi_cdate': forms.DateInput(attrs={'type': 'date'}),
            'vi_tdate': forms.DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'vi'

class TbRansomForm(forms.ModelForm):
    class Meta:
        model = TbRansom
        exclude = ('beneficCom',)
        widgets = {
            'ra_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'ra_cdate': forms.DateInput(attrs={'type': 'date'}),
            'ra_tdate': forms.DateInput(attrs={'type': 'date'}),
        }

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


class CheckBnumberForm(forms.Form):
    bnumber = forms.CharField(max_length=100, label='사업자등록번호')

    def clean_bnumber(self):
        bnumber = self.cleaned_data['bnumber']
        if TbBeneficcom.objects.filter(bc_cu_bnumber=bnumber):
            raise forms.ValidationError(' "%s"는 이미 사용중인 사업자등록번호 입니다.'%bnumber)
        return bnumber

class CheckIpsForm(forms.Form):
    pat_name = forms.CharField(max_length=100, label='IPS 탐지 패턴명')

    def clean_ips(self):
        pat_name = self.cleaned_data['pat_name']
        if DetectionPat.objects.filter(pat_name=pat_name):
            raise forms.ValidationError(' "%s"는 이미 사용중인 사업자등록번호 입니다.'%pat_name)
        return pat_name

class CommentForm(forms.ModelForm):
    com_class = forms.ChoiceField(choices=choices.com_class, required=False)
    class Meta:
        model = Comment
        exclude = ('model_name','model_pk')
