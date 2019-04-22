from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .models import User
from .models import Major
from .models import Question
from .models import Answer


from django.contrib.auth.models import User
from .serializers import (UserCreateSerializer, QuestionCreateSerializer,
                          QuestionListSerializer, AnswerCreateSerializer, AnswerListSerializer, MajorSerializer, ExpertUserCreateSerializer,QuestionCreateUpdateSerializer )

from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)
from .models import (User, Question, Answer, Major,)
from rest_framework import status
from rest_framework.response import Response



class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ExpertUserCreateAPIView(CreateAPIView):
    serializer_class = ExpertUserCreateSerializer


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    # permission_classes = [IsAuthenticated, ]


    def perform_create(self, serializer):
        serializer.save()

class QuestionDelete(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'
    # permission_class = [IsAdminUser,]


class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerCreateSerializer


    def post(self, request, question_id):
        my_data = request.data
        print(my_data)
        serializer = self.serializer_class(data=my_data)
        if serializer.is_valid():
            valid_data = serializer.data
            new_data = {
                'a_text': valid_data['a_text'],
                'question': Question.objects.get(id=question_id)
            }
            Answer.objects.create(**new_data)
            return Response(valid_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerListView(ListAPIView):

    def get(self, request, question_id):
        answers = Answer.objects.filter(
            question=Question.objects.get(id=question_id))
        message_list = AnswerListSerializer(answers, many=True).data
        return Response(message_list, status=status.HTTP_200_OK)



class MajorListView(ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
