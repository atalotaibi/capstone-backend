from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model




class User(AbstractUser):
    is_expert = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)





    # def __str__(self):
    #     return self.is_expert.username
   
    
    # Major = models.CharField(
    #     max_length=2,
    #     choices=MAJORS_CHOICES,
    #     default=null,
    # )

    # Major = models.ForeignKey(
    #     Major, related_name='users', default=1, on_delete=models.CASCADE)



class Major(models.Model):
    # name = models.CharField(max_length=40)
    COMPUTER_SCIENCE = 'Computer Science'
    COMMUNICATIONS = 'Communications'
    POLITICAL_SCIENCE = 'Political Science'
    BUSINESS = 'Business'
    ECONOMICS = 'Economics'
    PSYCHOLIGY = 'Psychology'
    MATH = 'Math'
    BIOLOGY = 'Biology'
    INFORMATION_SYSTEM_TECHNOLOGY = 'Information System Technology'
    CYBER_SECURITY = 'Cyber Security'
    HUMAN_RESUORCE = 'Humen Resuorce'
    ACCOUNTING = 'Accounting'
    ELECTRICAL_ENGINEERING = 'Electrical Engineering'
    MECHANICAL_ENGINEERING = 'Mechanical Engineering'
    BIOMEDICAL_ENGINEERING = 'Biomedical Engineering'
    MAJORS_CHOICES = (
        ('COMPUTER SCIENCE', 'Computer Science'),
        ('COMMUNICATIONS', 'Communications'),
        ('POLITICAL SCIENCE', 'Political Science'),
        ('BUSINESS', 'Business'),
        ('ECONOMICS', 'Economics'),
        ('PSYCHOLIGY', 'Psychology'),
        ('MATH', 'Math'),
        ('BIOLOGY', 'Biology'),
        ('INFORMATION SYSTEM TECHNOLOGY', 'Information System Technology'),
        ('CYBER SECURITY', 'Cyber Security'),
        ('HUMAN RESUORCE ', 'Humen Resuorce '),
        ('ACCOUNTING', 'Accounting'),
        ('ELECTRICAL ENGINEERING', 'Electrical Engineering'),
        ('MECHANICAL ENGINEERING', 'Mechanical Engineering'),
        ('BIOMEDICAL ENGINEERING', 'Biomedical Engineering'),

    )
    name = models.CharField(max_length= 23 , choices=MAJORS_CHOICES)

class Question(models.Model):
    q_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    asked_by = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
        related_name= "questions",
        null=True, blank=True
        )
    major = models.ForeignKey(
        Major, related_name='questions', default=1, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_on']

    def answered(self):
        return self.answers.exists()


class Answer(models.Model):
    a_text = models.TextField()
    question = models.ForeignKey(
        Question, related_name='answers', default=1, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
        related_name= "answers",
        null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']