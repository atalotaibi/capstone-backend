from django.urls import path
from .views import (UserCreateAPIView, QuestionCreateView,
                    QuestionListView, AnswerCreateView, AnswerListView, MajorListView, QuestionDelete, QuestionDetailView, AnswerApproveView)
from rest_framework_jwt.views import obtain_jwt_token

from .views import (
    UserCreateAPIView,
    ExpertUserCreateAPIView,
    UserDetailView,
    UserUpdateView,
    QuestionApproveView
)


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('user/detail/<int:user_id>/',
         UserDetailView.as_view(), name='user-detail'),
    path('user/update/<int:user_id>/',
         UserUpdateView.as_view(), name='user-update'),
    path('expert/register/', ExpertUserCreateAPIView.as_view(),
         name='expert_register'),


    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:question_id>/delete/',
         QuestionDelete.as_view(), name='question-delete'),
    path('question/list/', QuestionListView.as_view(), name='question-list'),
    path('question/<int:question_id>',
         QuestionDetailView.as_view(), name='question-detail'),
    path('<int:question_id>/', AnswerListView.as_view(), name='answer-list'),
    path('<int:question_id>/qstatus',
         QuestionApproveView.as_view(), name='question-approve'),
    path('<int:question_id>/send', AnswerCreateView.as_view(), name='answer-create'),
    path('<int:answer_id>/status/',
         AnswerApproveView.as_view(), name='answer-approve'),
    path('major/list/', MajorListView.as_view(), name='major-list'),


]
