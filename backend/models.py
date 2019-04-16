from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_expert = models.BooleanField(default=True)


class Major(models.Model):
    name = models.CharField(max_length=40)


class Question(models.Model):
    q_text = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    answered = models.BooleanField(default=False)

    approved = models.BooleanField(default=False)

    major = models.ForeignKey(
        Major, related_name='questions', default=1, on_delete=models.CASCADE)


class Answer(models.Model):
    a_text = models.TextField()
    question = models.ForeignKey(
    Question, related_name='answers', default=1, on_delete=models.CASCADE)
