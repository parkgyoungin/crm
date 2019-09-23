from django import forms
from post.models import RansomwarePost, Outflow
from post.my_def import to_date_widget

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

    weekness1 = forms.BooleanField()
    weekness2 = forms.BooleanField()
    weekness3 = forms.BooleanField()
    weekness4 = forms.BooleanField()
    weekness5 = forms.BooleanField()
    weekness6 = forms.BooleanField()
    weekness7 = forms.BooleanField()
    weekness8 = forms.BooleanField()
    weekness9 = forms.BooleanField()
    weekness10 = forms.BooleanField()
    weekness11 = forms.BooleanField()
    weekness12 = forms.BooleanField()

    class Meta:
        model = Outflow
        fields = '__all__'
