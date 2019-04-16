from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from .serializers import (
    UserCreateSerializer,  
)
from .models import User
from .models import Major
from .models import Question
from .models import Answer
from django.contrib.auth.models import User
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser
)
# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer