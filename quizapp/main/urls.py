from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    path('all-categories', views.all_categories, name='all_categories'),
]
