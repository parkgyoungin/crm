from django import forms
from post.models import Timetable, Notice, Takeover
from django_summernote.widgets import SummernoteWidget
from post.my_def import to_date_widget

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        exclude = ('user', 'views')
        widgets = {
            'content': SummernoteWidget,
        }

class NoticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = Notice
        exclude = ('user', 'views')
        widgets = {
            'content': SummernoteWidget,
        }

class TakeoverForm(forms.ModelForm):
    class Meta:
        model = Takeover
        exclude = ('user', 'views')
        widgets = {
            'content': SummernoteWidget,
        }