from django.urls import path
from .views import (UserCreateAPIView, QuestionCreateView, QuestionListView, AnswerCreateView)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/list/', QuestionListView.as_view(), name='question-list'),
    path('Answer/list/', AnswerCreateView.as_view(), name='Answer-list'),
]
