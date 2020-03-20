from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer



class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users,many=True)
        return Response(serializers.data)
    def post(self,request,format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
