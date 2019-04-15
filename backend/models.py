from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_expert = models.BooleanField(default=True)


class Major(models.Model):
    name = models.CharField(max_length=40)


class Question(models.Model):
    q_text = models.TextField()
    ANSWEREd = (
        ('T', 'true'),
        ('F', 'false'),
    )
    question_status = models.CharField(
        max_length=2,
        choices=ANSWEREd,
        default='F',
    )
    APPROVED = (
        ('T', 'true'),
        ('F', 'false'),
    )
    answer_status = models.CharField(
        max_length=2,
        choices=APPROVED,
        default='F',
    )
    major = models.ForeignKey(
        Major, related_name='questions', default=1, on_delete=models.CASCADE)


class Answer(models.Model):
    a_text = models.TextField()
    question = models.ForeignKey(
        Question, related_name='answers', default=1, on_delete=models.CASCADE)
