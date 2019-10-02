from django import forms
from post.models import DetectionPattern, IPSTune
from post.my_def import to_date_widget
from choice.choices import get_choices
from django_summernote.widgets import SummernoteWidget

class DetectionPatternForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DetectionPatternForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)
        self.fields['pattern_name'].widget.attrs['readonly'] = 'true'
        self.fields['content'].widget = SummernoteWidget()
        self.fields['equipment_class'] = forms.ChoiceField(widget=forms.RadioSelect, choices=get_choices('se_equipment_class',defalut=False))
        self.fields['attack_class'] = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'set_sub_list(this)'}), choices=get_choices('attack_class',defalut=False))

        subs = get_choices('attack_class_sub1')+get_choices('attack_class_sub2', defalut=False)+get_choices('attack_class_sub3',defalut=False)+get_choices('attack_class_sub4', defalut=False)
        self.fields['attack_type'] = forms.ChoiceField(widget=forms.Select, choices=subs)

        self.fields['attack_class_etc'].widget.attrs['placeholder'] = '기타선택시 입력하세요'
        self.fields['attack_type_etc'].widget.attrs['placeholder'] = '기타선택시 입력하세요'

    class Meta:
        model = DetectionPattern
        fields = '__all__'


class IPSTuneForm(forms.ModelForm):
    class Meta:
        model = IPSTune
        #fields = '__all__'
        exclude = ('user', 'views')
        widgets = {
            'content': SummernoteWidget,
        }


