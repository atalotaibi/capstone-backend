from django.urls import path
from .views import (UserCreateAPIView, QuestionCreateView,
                    QuestionListView, AnswerCreateView, AnswerListView)
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/list/', QuestionListView.as_view(), name='question-list'),
    path('<int:question_id>/', AnswerListView.as_view(), name='Answer-list'),
    path('<int:question_id>/send', AnswerCreateView.as_view(), name='Answer-create'),
]
