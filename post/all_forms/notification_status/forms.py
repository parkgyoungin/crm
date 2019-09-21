from django import forms
from post.models import RansomwarePost
from post.my_def import to_date_widget

class RansomwarePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RansomwarePostForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = RansomwarePost
        fields = '__all__'
