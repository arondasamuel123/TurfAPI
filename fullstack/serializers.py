from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password','role_type')
        
    def validate_password(self, value: str) -> str:
        return make_password(value)

        
    