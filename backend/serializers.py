from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (Question, Answer, Major,)

class MajorSerializer(serializers.ModelSerializer): 
	
	class Meta:
		model = Major
		fields = ['name']


class QuestionCreateSerializer(serializers.ModelSerializer):


	class Meta:
		model = Question
		fields = ['q_text', 'major',]




class AnswerListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ['a_text']


class QuestionListSerializer(serializers.ModelSerializer):
	answers = AnswerListSerializer(many=True)
	major = MajorSerializer()
	class Meta:
		model = Question
		fields = ['q_text', 'created_on','answers', 'major',]
		


class AnswerCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Answer
		fields = ['a_text',]






