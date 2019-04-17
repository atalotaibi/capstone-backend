from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from django.contrib.auth.models import User
from .serializers import (UserCreateSerializer, QuestionCreateSerializer,
                          QuestionListSerializer, AnswerCreateSerializer, MajorSerializer)
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)
from .models import (User, Question, Answer, Major,)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    # permission_classes = [IsAuthenticated, ]

    # def perform_create(self, serializer):
    # 	serializer.save()


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
