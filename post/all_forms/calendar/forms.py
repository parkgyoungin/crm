from django import forms
from post.models import Schedule, Attendance
from post.my_def import to_date_widget

class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        to_date_widget(self.fields)

    class Meta:
        model = Schedule
        exclude = ('user','views')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ('user', )