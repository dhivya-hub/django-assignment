from rest_framework import serializers
from .models import *


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta(object):
#         model = User
#         fields = ('id','username','password')
#         extra_kwargs = {'password': {'write_only': True}}


class SubjectSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.subject

    class Meta:
        model = Subject


class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True,read_only=False)

    # subject = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject']


class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=False, many=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Student
        fields = ['id', 'user', 'teacher']
