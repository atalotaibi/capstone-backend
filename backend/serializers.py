# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import (
  User,
  Major,
  Question,
  Answer,
)

User = get_user_model()
def assign_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email',]


class BaseCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'first_name', 'last_name', 'email', 'token', ]


class UserCreateSerializer(BaseCreateSerializer):
    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.is_expert = False
        new_user.set_password(validated_data['password'])
        new_user.save()
        token = assign_token(new_user)
        validated_data['token'] = token
        return validated_data


class ExpertUserCreateSerializer(BaseCreateSerializer):
    def create(self, validated_data):        
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        token = assign_token(new_user)
        validated_data['token'] = token
        return validated_data


class UserDetailSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
# im gonna finish the profile today hell yeah
    # image = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','is_expert','username',
                  'first_name', 'last_name', 'email', ]

class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username',
                  'first_name', 'last_name', 'email','user' ]
class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = ['name']


class QuestionCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Question
        fields = ['q_text', 'major',]


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['a_text']


class QuestionListSerializer(serializers.ModelSerializer):
    answered = serializers.SerializerMethodField()
    major = MajorSerializer()

    class Meta:
        model = Question
        fields = ['id', 'q_text', 'created_on', 'answers', 'major', ]

    def get_answered(self, obj):
        return obj.answered()




class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['a_text', ]

