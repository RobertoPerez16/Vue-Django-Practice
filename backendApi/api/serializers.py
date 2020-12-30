from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import ToDo
from django.contrib.auth.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id','title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        extra_kwargs = {'password': {'required': True , 'write_only': True }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
