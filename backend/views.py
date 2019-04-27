from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .models import User, Major, Question, Answer
from django.contrib.auth import get_user_model


# from django.contrib.auth.models import User
from .serializers import (UserCreateSerializer, QuestionCreateSerializer,
                          QuestionListSerializer, AnswerCreateSerializer, AnswerListSerializer, MajorSerializer, ExpertUserCreateSerializer, QuestionCreateUpdateSerializer, QuestionDetailSerializer, AnswerApproveSerializer, QuestionApproveSerializer, UserDetailSerializer,
    UserCreateUpdateSerializer)

from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response




class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    def perform_create(self, serializer):
        print("2")
        super().perform_create(serializer)
        



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


class QuestionCreateView(CreateAPIView):
    serializer_class = QuestionCreateSerializer
    # permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        
        serializer.save(asked_by=self.request.user)
        

class QuestionDelete(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'
    # permission_class = [IsAdminUser,]



class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    # A = [AllowAny,IsAuthenticated, IsAdminUser ]
    

class QuestionDetailView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerCreateSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]


    def perform_create(self, serializer):
        
        serializer.save(asked_by=self.request.user)

    def post(self, request, question_id):
        my_data = request.data
        print(my_data)
        serializer = self.serializer_class(data=my_data)
        if serializer.is_valid():
            valid_data = serializer.data
            new_data = {
                'a_text': valid_data['a_text'],
                'question': Question.objects.get(id=question_id),
                'answered_by': request.user
            }
            Answer.objects.create(**new_data)
            return Response(valid_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerListView(ListAPIView):
    serializer_class = AnswerListSerializer
    # permission_classes = [AllowAny,IsAuthenticated, IsAdminUser ]

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


class QuestionApproveView(RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionApproveSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'question_id'
