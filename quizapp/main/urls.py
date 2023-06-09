from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/register', views.register, name='register'),
    path('all-categories', views.AllCategoriesListView.as_view(), name='all_categories'),
    path('category-questions/<int:cat_id>', views.category_questions, name='category_questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', views.submit_answer, name='submit_answer'),
    path('attempt-limit/', views.AttemptLimitView.as_view(), name='attempt-limit'),
    path('result/', views.result, name='result'),
    path('all-users', views.AllUsersListView.as_view(), name='all-users'),
    path('profile/', views.ProfileDetail.as_view(), name='profile'),
]
