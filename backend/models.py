from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_expert = models.BooleanField(default=True)

    # Major = models.CharField(
    #     max_length=2,
    #     choices=MAJORS_CHOICES,
    #     default=null,
    # )

    # Major = models.ForeignKey(
    #     Major, related_name='users', default=1, on_delete=models.CASCADE)


class Major(models.Model):
    name = models.CharField(max_length=40)


class Question(models.Model):
    q_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    asked_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="asked_by"
    )
    major = models.ForeignKey(
        Major, related_name='questions', default=1, on_delete=models.CASCADE)

    def answered(self):
        return self.answers.exists()


class Answer(models.Model):
    a_text = models.TextField()
    question = models.ForeignKey(
        Question, related_name='answers', default=1, on_delete=models.CASCADE)
