from django import forms
from . import choices
from django_summernote.widgets import SummernoteWidget
from django.utils.safestring import mark_safe
from main.models import *
from .models import *

#https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms
class WriteCompany(forms.Form):
    #업체명
    cu_name = forms.CharField(
        max_length=50,
    )

    #입주기업
    cu_tenant= forms.BooleanField()

    #관리번호
    cu_cnumber = forms.CharField(
        max_length=20
    )

    #서비스현황-보안관제
    cu_serstate_security = forms.ChoiceField(
        choices=choices.serstate,
    )

    #서비스현황-내부정보
    cu_serstate_information = forms.ChoiceField(
        choices=choices.serstate
    )

    #서비스현황-악성코드
    cu_serstate_virus = forms.ChoiceField(
        choices=choices.serstate
    )

    #서비스현황-랜섬웨어
    cu_serstate_ransomware = forms.ChoiceField(
        choices=choices.serstate
    )

    #허수현황-보안관제
    cu_imastate_security = forms.BooleanField()

    #허수현황-내부정보
    cu_imastate_information = forms.BooleanField()

    #허수현황-악성코드
    cu_imastate_virus = forms.BooleanField()

    #허수현황-랜섬웨어
    cu_imastate_ransomware = forms.BooleanField()

    #업태
    cu_business = forms.ChoiceField(
        choices=choices.sample
    )

    #업종
    cu_comclass = forms.ChoiceField(
        choices=choices.sample
    )

    #가입경로
    cu_path = forms.ChoiceField(
        choices=choices.sample
    )

    #대표자명
    cu_rname = forms.CharField(
        max_length=50
    )

    #대표자 이메일
    cu_remail = forms.EmailField()

    #홈페이지
    cu_homepage = forms.URLField()

    #사업자번호
    cu_bnumber = forms.CharField(
        max_length=50
    )

    #주소
    cu_address = forms.CharField(
        max_length=100
    )

    #설치주소
    cu_iaddress = forms.CharField(
        widget=forms.Textarea
    )

    #대규모 입주단지
    op_imove = forms.ChoiceField(
        choices=choices.sample
    )

    #대기업 협력사
    op_lpartner = forms.ChoiceField(
        choices=choices.sample
    )

    #패쇄망
    op_closer = forms.ChoiceField(
        choices=choices.sample
    )

    #방위산업
    op_defense = forms.ChoiceField(
        choices=choices.sample
    )

    #기타
    op_etc = forms.CharField(
        max_length=100
    )

    #계약사항
    se_contract = forms.ChoiceField(
        choices=choices.sample
    )

    #선차단 권한
    se_pblock = forms.CharField(
        max_length=100
    )

    #보고서 발송일
    se_sdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #연동일
    se_cdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #시리얼번호
    se_serial = forms.CharField(
        max_length=100
    )

    #라이선스 만료일
    se_edate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #장비펌웨어
    se_firmware = forms.CharField(
        max_length=100
    )

    #장비분류
    se_eqclass = forms.CharField(
        max_length=100
    )

    #소유권
    se_ownership = forms.ChoiceField(
        choices=choices.sample
    )

    #접근권한
    se_access = forms.CharField(
        max_length=100
    )

    #ips/check
    se_ipsrule = forms.BooleanField()

    #ips/check
    se_syslog = forms.BooleanField()

    #ips/check
    se_icmp = forms.BooleanField()

    #ips/check
    se_snmp = forms.BooleanField()

    #해지일
    se_tdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일 사유
    se_treason = forms.CharField(
        max_length=100
    )

    #기타사항
    se_etc = forms.CharField(
        widget=forms.Textarea
    )


    #계약사항
    in_contract = forms.ChoiceField(
        choices=choices.sample
    )

    #신청대수
    in_apply = forms.IntegerField()

    #연동일
    in_cdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #ip
    in_ip = forms.CharField(
        widget=forms.Textarea
    )

    #해지일
    in_tdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일-사유
    in_treason = forms.CharField(
        max_length=100
    )

    #기타사항
    in_etc = forms.CharField(
        widget=forms.Textarea
    )

    #계약사항
    vi_contract = forms.ChoiceField(
        choices=choices.sample
    )

    #신청대수
    vi_apply = forms.IntegerField()

    #연동일
    vi_cdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일
    vi_tdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일-사유
    vi_treason = forms.CharField(
        max_length=100
    )

    #기타사항
    vi_etc = forms.CharField(
        widget=forms.Textarea
    )

    #계약사항
    ra_contract = forms.ChoiceField(
        choices=choices.sample
    )

    #신청대수
    ra_apply = forms.IntegerField()

    #연동일
    ra_cdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일
    ra_tdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    #해지일-사유
    ra_treason = forms.CharField(
        max_length=100
    )

    #기타사항
    ra_etc = forms.CharField(
        widget=forms.Textarea
    )

    #정:이름
    ma_name = forms.CharField(
        max_length=100
    )

    #정:부서
    ma_circles = forms.CharField(
        max_length=100
    )

    #정:휴대폰
    ma_phone = forms.IntegerField()

    #정:회사전화
    ma_cphone = forms.IntegerField()

    #정:이메일
    ma_email = forms.EmailField()

    # 부:이름
    re_name = forms.CharField(
        max_length=100
    )

    # 부:부서
    re_circles = forms.CharField(
        max_length=100
    )

    # 부:휴대폰
    re_phone = forms.IntegerField()

    # 부:회사전화
    re_cphone = forms.IntegerField()

    # 부:이메일
    re_email = forms.EmailField()

    # 요금:이름
    ch_name = forms.CharField(
        max_length=100
    )

    # 요금:부서
    ch_circles = forms.CharField(
        max_length=100
    )

    # 요금:휴대폰
    ch_phone = forms.IntegerField()

    # 요금:회사전화
    ch_cphone = forms.IntegerField()

    # 요금:이메일
    ch_email = forms.EmailField()

    #세금계산서발송일
    bc_sdate = forms.IntegerField()

    #기타사항
    bc_etc = forms.CharField(
        widget=forms.Textarea
    )

    #첨부파일
    bc_file = forms.FileField(
        widget=forms.FileInput
    )


class BeneficComForm(forms.ModelForm):
    cu_bnumber_h = forms.CharField(widget=forms.HiddenInput)
    class Meta:
        model = BeneficCom
        fields = '__all__'
        widgets = {
            'cu_serstate_security': forms.Select(choices=choices.serstate, attrs={'required':'true'} ),

            'cu_serstate_information': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'cu_serstate_virus': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'cu_serstate_ransomware': forms.Select(choices=choices.serstate, attrs={'required': 'true'}),

            'cu_business': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'cu_comclass': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'cu_path': forms.Select(choices=choices.sample, attrs={'required': 'true'}),

            'op_imove': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'op_lpartner': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'op_closer': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'op_defense': forms.Select(choices=choices.op, attrs={'required': 'true', 'disabled':'true'}),

            'cu_bnumber': forms.TextInput(attrs={'onclick':'popup_idChk()'}),

            'bc_sdate': forms.DateInput(attrs={'type':'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'be'

class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        exclude = ('beneficCom',)
        widgets = {
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

class InternalForm(forms.ModelForm):
    class Meta:
        model = Internal
        exclude = ('beneficCom',)
        widgets = {
            'in_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'in_cdate': forms.DateInput(attrs={'type': 'date'}),
            'in_tdate': forms.DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'in'

class VirusForm(forms.ModelForm):
    class Meta:
        model = Virus
        exclude = ('beneficCom',)
        widgets = {
            'vi_contract': forms.Select(choices=choices.sample, attrs={'required': 'true'}),
            'vi_cdate': forms.DateInput(attrs={'type': 'date'}),
            'vi_tdate': forms.DateInput(attrs={'type': 'date'}),
        }

    @staticmethod
    def get_prefix():
        return 'vi'

class RansomwareForm(forms.ModelForm):
    class Meta:
        model = Ransomware
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
        if BeneficCom.objects.filter(cu_bnumber=bnumber):
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
    class Meta:
        model = Comment
        exclude = ('model',)

