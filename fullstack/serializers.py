from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','password','role_type')
        
    def validate_password(self, value: str) -> str:
        return make_password(value)
    
class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenSerializer, self).validate(attrs)
        data.update({'id':self.user.id})
        data.update({'user':self.user.username})
        data.update({'email':self.user.email})
        data.update({'role_type':self.user.role_type})

        return data

        
    