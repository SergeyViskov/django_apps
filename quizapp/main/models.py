from django.db import models
from django.contrib.auth.models import User


class QuizCategory(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class QuizQuestions(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    right_opt = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'User Submitted Answer'
    
    def __str__(self):
        return str(self.question)


class UserCategoryAttempts(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Attempts Category'
    
    def __str__(self):
        return str(self.category)


class UserPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'User Points'
    
    def __str__(self):
        return str(self.user)
