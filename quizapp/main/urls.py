from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    path('all-categories', views.all_categories, name='all_categories'),
    path('category-questions/<int:cat_id>', views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer, name='submit_answer'),
    path('attempt-limit/', views.attempt_limit, name='attempt-limit'),
    path('result/', views.result, name='result'),
    path('all-users/', views.all_users, name="all-users")
]
