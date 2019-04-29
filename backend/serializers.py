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
    return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'image', 'is_expert']


class BaseCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password',
                  'first_name', 'last_name', 'email', 'token', 'image']


# get the token

class UserCreateSerializer(BaseCreateSerializer):
    # pass
    def create(self, validated_data):
        user_obj = super().create(validated_data)
        user_obj.set_password(user_obj.password)
        user_obj.save()
        user_obj.token = assign_token(user_obj)
        return user_obj


class ExpertUserCreateSerializer(BaseCreateSerializer):
    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        token = assign_token(new_user)
        validated_data['token'] = token
        return validated_data


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ['id', 'is_expert', 'username',
                  'first_name', 'last_name', 'email', 'image']


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',
                  'first_name', 'last_name', 'email', 'user', 'image']


class MajorSerializer(serializers.ModelSerializer):
    # major = serializers.SerializerMethodField()

    class Meta:
        model = Major
        fields = ['id', 'major']

    # def get_major(self, obj):
    #     return obj.major

        # shows the name


class QuestionCreateSerializer(serializers.ModelSerializer):
    asked_by = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['q_text', 'major', 'asked_by']


class QuestionApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['approved']


class AnswerListSerializer(serializers.ModelSerializer):
    answered_by = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'a_text', 'created_on', 'answered_by', 'approved']


class QuestionListSerializer(serializers.ModelSerializer):
    asked_by = UserSerializer(read_only=True)
    answered = serializers.SerializerMethodField()
    major = MajorSerializer()

    class Meta:
        model = Question
        fields = ['id', 'q_text', 'created_on', 'answers',
                  'major', 'answered', 'asked_by', 'approved']

    def get_answered(self, obj):
        return obj.answered()

    # def get_major(self, obj):
    #     return obj.major.name

    def get_asked_by(self, obj):
        return obj.asked_by.name()


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['a_text', ]


class AnswerApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['approved', ]


class QuestionDetailSerializer(serializers.ModelSerializer):
    asked_by = UserSerializer(read_only=True)
    major = MajorSerializer()
    class Meta:
        model = Question
        fields = ['id', 'q_text', 'created_on',
                  'answers', 'major', 'answered', 'approved', 'asked_by']
