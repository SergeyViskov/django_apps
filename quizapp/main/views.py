from django.shortcuts import render

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
