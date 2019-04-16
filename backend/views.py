from django.shortcuts import render
from rest_framework.generics import (
	CreateAPIView, 
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	DestroyAPIView,
)
from .serializers import (QuestionCreateSerializer, QuestionListSerializer,AnswerCreateSerializer, MajorSerializer )
from rest_framework.permissions import (IsAuthenticated, IsAdminUser, )
from .models import (Question, Answer, Major,  )

class QuestionCreateView(CreateAPIView):
	serializer_class = QuestionCreateSerializer
	# permission_classes = [IsAuthenticated, ]

	def perform_create(self, serializer):
		serializer.save()

class QuestionListView(ListAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionListSerializer


class AnswerCreateView(CreateAPIView):
	serializer_class = AnswerCreateSerializer
	# permission_classes = [IsAuthenticated, ]

	def perform_create(self, serializer):
		serializer.save()

# class AnswerListView(ListAPIView):
# 	queryset = Answer.objects.all()
# 	serializer_class = QuestionListSerializer