from django import forms
from post.models import Answer
from django_summernote.widgets import SummernoteWidget

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title', 'content']
        #exclude = ('content_type', 'object_id')
        widgets = {
            'content': SummernoteWidget,
        }