from django.contrib import admin

from . import models


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    ilst_display = ['id', 'question', 'user', 'right_answer']


admin.site.register(models.QuizCategory)
admin.site.register(models.QuizQuestions, QuizQuestionAdmin)
admin.site.register(models.UserSubmittedAnswer, UserSubmittedAnswerAdmin)
