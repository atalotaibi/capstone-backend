from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateAPIView,
    ExpertUserCreateAPIView
)

urlpatterns = [
     ## Auth ##
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('expert/register/', ExpertUserCreateAPIView.as_view(), name='expert_register'),

]
