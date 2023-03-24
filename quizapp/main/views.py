from datetime import timedelta

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import generic
from django.utils.decorators import method_decorator

from . import forms
from . import models


class HomeView(generic.TemplateView):
    template_name = 'home.html'


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
        'msg': msg,
    }
    return render(request, 'registration/register.html', context)


@method_decorator(login_required, name='dispatch')
class AllCategoriesListView(generic.ListView):
    model = models.QuizCategory
    template_name = 'all-category.html'


@login_required
def category_questions(request, cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestions.objects.filter(
        category=category).order_by('id').first()
    last_attempt = None
    future_time = None
    hours_limit = 24
    count_attempt = models.UserCategoryAttempts.objects.filter(
        user=request.user, category=category).count()
    if count_attempt == 0:
        models.UserCategoryAttempts.objects.create(
            user=request.user, category=category)
    else:
        last_attempt = models.UserCategoryAttempts.objects.filter(
            user=request.user, category=category).order_by('-id').first()
        future_time = last_attempt.attempt_time + timedelta(hours=hours_limit)
        if last_attempt and last_attempt.attempt_time < future_time:
            return redirect('attempt-limit')
        else:
            models.UserCategoryAttempts.objects.create(
                user=request.user, category=category)
    context = {
        'question': question,
        'category': category,
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
            'category': category,
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
            return result(request)
    else:
        return HttpResponse('Method not allowed!')


@method_decorator(login_required, name='dispatch')
class AttemptLimitView(generic.TemplateView):
    template_name = 'attempt-limit.html'


@login_required
def result(request):
    result = models.UserSubmittedAnswer.objects.filter(user=request.user)
    skipped = models.UserSubmittedAnswer.objects.filter(
        user=request.user, right_answer='Not Submitted').count()
    attempted = models.UserSubmittedAnswer.objects.filter(
        user=request.user).exclude(right_answer='Not Submitted').count()
    right_ans = 0
    for row in result:
        if row.question.right_opt == row.right_answer:
            right_ans += 1
    try:
        add_score = models.UserPoints.objects.get(user=request.user)
        add_score.points = right_ans
        add_score.save()
    except models.UserPoints.DoesNotExist:
        add_score = models.UserPoints(user=request.user, points=right_ans)
        add_score.save()
    context_results = {
        'result': result,
        'total_skipped': skipped,
        'attemped': attempted,
        'right_ans': right_ans,
        'points': add_score,
    }
    return render(request, 'result.html', context_results)


@method_decorator(login_required, name='dispatch')
class AllUsersListView(generic.ListView):
    model = models.UserPoints
    template_name = 'all-users.html'


@method_decorator(login_required, name='dispatch')
class ProfileDetail(generic.View):

    def get(self, request):
        user = models.UserPoints.objects.get(user=request.user)
        context = {
            'user': user,
        }
        return render(request, 'profile.html', context)
