from django import forms
from post.models import RansomwarePost, Outflow
from post.my_def import to_date_widget
from django_summernote.widgets import SummernoteWidget

class RansomwarePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RansomwarePostForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)
        self.fields['send_date'].widget.attrs['onchange'] = 'set_process_state(this)'

    class Meta:
        model = RansomwarePost
        fields = '__all__'

class OutflowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OutflowForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)
        self.fields['send_date'].widget.attrs['onchange'] = 'set_process_state(this)'
        self.fields['content'].widget = SummernoteWidget()

    weekness1 = forms.BooleanField(label='인젝션', label_suffix='', required=False)
    weekness2 = forms.BooleanField(label='파일다운로드', label_suffix='', required=False)
    weekness3 = forms.BooleanField(label='웹서비스 메소드 설정공격', label_suffix='', required=False)
    weekness4 = forms.BooleanField(label='파일 업로드', label_suffix='', required=False)
    weekness5 = forms.BooleanField(label='단계별 접근제한 실패', label_suffix='', required=False)
    weekness6 = forms.BooleanField(label='약한 문자열 강도', label_suffix='', required=False)
    weekness7 = forms.BooleanField(label='크로스사이트', label_suffix='', required=False)
    weekness8 = forms.BooleanField(label='스크립트(XSS)', label_suffix='', required=False)
    weekness9 = forms.BooleanField(label='관리자페이지 노출', label_suffix='', required=False)
    weekness10 = forms.BooleanField(label='디렉토리 리스팅', label_suffix='', required=False)
    weekness11 = forms.BooleanField(label='데이터 평문 전송', label_suffix='', required=False)
    weekness12 = forms.BooleanField(label='정보노출', label_suffix='', required=False)

    class Meta:
        model = Outflow
        fields = '__all__'

