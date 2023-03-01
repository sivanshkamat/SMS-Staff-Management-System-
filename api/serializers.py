from rest_framework import serializers
from .models import StudentModel,SubjectModel,TeacherModel
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'
    
class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model=TeacherModel
        fields='__all__'
        
        
class SubjectSerializers(serializers.ModelSerializer):
    user=UserSerializer(write_only=True)
    class Meta:
        model=SubjectModel
        fields=['roll', 'name', 'email', 'phone_no', 'city', 'user']
        