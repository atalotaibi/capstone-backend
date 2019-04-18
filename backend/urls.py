from django.urls import path
from .views import (
UserCreateAPIView,
QuestionCreateView,
QuestionListView, 
AnswerCreateView, 
AnswerListView, 
MajorListView, 
UserCreateAPIView,
ExpertUserCreateAPIView)
from rest_framework_jwt.views import obtain_jwt_token





urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('expert/register/', ExpertUserCreateAPIView.as_view(), name='expert_register'),


    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/list/', QuestionListView.as_view(), name='question-list'),
    path('<int:question_id>/', AnswerListView.as_view(), name='answer-list'),
    path('<int:question_id>/send', AnswerCreateView.as_view(), name='answer-create'),
    path('major/list/', MajorListView.as_view(), name='major-list'),

