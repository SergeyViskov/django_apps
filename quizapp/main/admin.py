from django.contrib import admin

from . import models


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    ilst_display = ['id', 'question', 'user', 'right_answer']


class UserCategoryAttemptsAdmin(admin.ModelAdmin):
    ilst_display = ['category', 'user', 'attempt_time']


class UserPointsAdmin(admin.ModelAdmin):
    ilst_display = ['user', 'points']


admin.site.register(models.QuizCategory)
admin.site.register(models.QuizQuestions, QuizQuestionAdmin)
admin.site.register(models.UserSubmittedAnswer, UserSubmittedAnswerAdmin)
admin.site.register(models.UserCategoryAttempts, UserCategoryAttemptsAdmin)
admin.site.register(models.UserPoints, UserPointsAdmin)
