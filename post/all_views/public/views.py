from django.shortcuts import render, HttpResponseRedirect, reverse
from post.models import Answer, Timetable, Takeover, Notice
from post.all_forms.public.forms import AnswerForm
from django.contrib.auth.decorators import login_required
from post.my_def import view
from django.conf import settings
from post.my_def import config_page_uri, delete_object

PAGE = 5
@login_required
def writeAnswer(request, model, id):
    object = eval('%s.objects.get(id=id)'%model)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.content_object = object
            answer.user = request.user
            answer.save()
            return HttpResponseRedirect(reverse('post:list', args=[model.lower()]))
    else:
        form = AnswerForm()
    return render(request, 'post/answer/write.html', {'form': form})

def detailAnswer(request, id):
    object = Answer.objects.get(id=id)
    model = object.content_type.model_class()
    view(object)
    uri = reverse('post:list', args=[model.__name__])
    if request.session[settings.LIST_CONDITIONS_ID].get(model.__name__):
        uri = config_page_uri(request, object.object_id, model.__name__, PAGE)

    return render(request, 'post/answer/detail.html', {'object':object, 'uri':uri})

@login_required
def updateAnswer(request, id):
    object = Answer.objects.get(id=id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post:answer_detail', args=[id]))

    else:
        form = AnswerForm(instance=object)

    return render(request, 'post/answer/write.html', {'form': form})

@login_required
def deleteAnswer(request, id):
    object = Answer.objects.get(id=id)
    model = object.content_type.model_class().__name__
    delete_object(Answer, id)

    return HttpResponseRedirect(reverse('post:list', args=[model.lower()]))