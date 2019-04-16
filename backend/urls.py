from django.urls import path
from .views import (QuestionCreateView, QuestionListView, AnswerCreateView)

urlpatterns = [
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/list/', QuestionListView.as_view(), name='question-list'),
    path('Answer/list/', AnswerCreateView.as_view(), name='Answer-list'),

]
