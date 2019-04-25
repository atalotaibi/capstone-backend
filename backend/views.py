from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)


from .serializers import (
    UserCreateSerializer,
    ExpertUserCreateSerializer,
    UserDetailSerializer,
    UserCreateUpdateSerializer
)


from .models import User, Major, Question, Answer
from django.contrib.auth import get_user_model


# from django.contrib.auth.models import User
from .serializers import (UserCreateSerializer, QuestionCreateSerializer,
                          QuestionListSerializer, AnswerCreateSerializer, AnswerListSerializer, MajorSerializer, ExpertUserCreateSerializer, QuestionCreateUpdateSerializer, QuestionDetailSerializer, AnswerApproveSerializer)

from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)
from rest_framework import status
from rest_framework.response import Response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ExpertUserCreateAPIView(CreateAPIView):
    serializer_class = ExpertUserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id'


class Majors(ListAPIView):

    url = "https://www.jvis.com/uguide/majordesc.htm"
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), features='html.parser')
    info = soup.findAll('a', attrs={'href': re.compile("#")})

    for i in info:
        print(i.text)


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    # permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save()


#  dont forgat to assign the user asked=self.request.user


class QuestionDelete(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'
    # permission_class = [IsAdminUser,]


class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionDetailView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'


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


class AnswerApproveView(RetrieveUpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerApproveSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'answer_id'
