from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import forms
from . import models


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    form = forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been added'
    context = {
        'form': form,
        'msg': msg
    }
    return render(request, 'registration/register.html', context)


def all_categories(request):
    cat_data = models.QuizCategory.objects.all()
    context = {
        'data': cat_data
    }
    return render(request, 'all-category.html', context)


@login_required
def category_questions(request, cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestions.objects.filter(
        category=category).order_by('id').first()
    context = {
        'question': question,
        'category': category
    }
    return render(request, 'category-questions.html', context)


@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method == 'POST':
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestions.objects.filter(
            category=category, id__gt=quest_id).exclude(
                id=quest_id).order_by('id').first()
        context = {
            'question': question,
            'category': category
        }
        if 'skip' in request.POST:
            if question:
                quest = models.QuizQuestions.objects.get(id=quest_id)
                user = request.user
                answer = 'Not Submitted'
                models.UserSubmittedAnswer.objects.create(
                    user=user, question=quest, right_answer=answer)
                return render(request, 'category-questions.html', context)
        else:
            quest = models.QuizQuestions.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            models.UserSubmittedAnswer.objects.create(
                    user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'category-questions.html', context)
        else:
            result = models.UserSubmittedAnswer.objects.filter(
                user=request.user)
            return render(request, 'result.html', {'result': result})
    else:
        return HttpResponse('Method not allowed!')
