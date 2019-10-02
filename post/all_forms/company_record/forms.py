from django import forms
from post.models import CompanyRecord
from post.my_def import to_date_widget
from choice.choices import get_choices
import datetime

def get_available(field, *args, **kwargs):
    title = None
    if kwargs.get('instance'):
        title = eval("kwargs['instance'].%s"%field)
    elif args:
        title = args[0][field]
    return title


class CompanyRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            kwargs['instance'].occurr_date = kwargs['instance'].occurr_date.strftime('%Y-%m-%dT%H:%M')
        occurr_date = get_available('occurr_date', *args, **kwargs)
        super(CompanyRecordForm, self).__init__(*args, **kwargs)
        self.fields['occurr_date'] = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'],widget=forms.TimeInput(attrs={'type': 'datetime-local'}))
        self.fields['company'].widget = forms.HiddenInput()
        self.fields['visible_m'].widget =forms.CheckboxInput()
        self.fields['visible_s'].widget = forms.CheckboxInput()
        self.fields['visible_e'].widget = forms.CheckboxInput()
        self.fields['process_method'] = forms.ChoiceField(choices=get_choices('process_method',defalut=False), widget=forms.RadioSelect)

        if occurr_date:
            print(occurr_date)
            #print(self.fields['occurr_date'].widget.attrs['value'])

    class Meta:
        model = CompanyRecord
        fields = '__all__'
