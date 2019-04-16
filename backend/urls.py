from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateAPIView
)

urlpatterns = [
     ## Auth ##
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

]
