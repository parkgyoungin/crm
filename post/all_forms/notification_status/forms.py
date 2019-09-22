from django import forms
from post.models import RansomwarePost
from post.my_def import to_date_widget

class RansomwarePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RansomwarePostForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)
        self.fields['send_date'].widget.attrs['onchange'] = 'set_process_state(this)'

    class Meta:
        model = RansomwarePost
        fields = '__all__'
