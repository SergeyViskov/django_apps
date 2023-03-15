from django.contrib import admin

from . import models


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(models.QuizCategory)
admin.site.register(models.QuizQuestions, QuizQuestionAdmin)
