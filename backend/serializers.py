from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import (

  User,
  Major,
  Question,
  Answer,

)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'first_name', 'last_name', 'email', 'token', ]

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']

        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_expert=False)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data




class ExpertUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password',
            'first_name', 'last_name', 'email', 'token', ]
    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_expert=True)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data




class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = ['name']


class QuestionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['q_text', 'major', ]

class QuestionCreateUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Question
        fields = ['q_text', 'major', ]


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['a_text']


class QuestionListSerializer(serializers.ModelSerializer):
    answered = serializers.SerializerMethodField()
    major = MajorSerializer()
    
    
    class Meta:
        model = Question
        fields = ['id', 'q_text', 'created_on', 'answers', 'major','answered', ]

    def get_answered(self, obj):
        return obj.answered()


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['a_text', ]

