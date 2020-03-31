from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Turf
from .serializers import UserSerializer,CustomTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import TurfSerializer
from .permissions import TurfOwner


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
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

class TurfView(APIView):
    permission_classes = (TurfOwner,)
    def post(self, request, format=None):
        serializers = TurfSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TurfList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        all_turfs = Turf.objects.all()
        serializers = TurfSerializer(all_turfs, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class SingleTurf(APIView):
    permission_classes = (TurfOwner,)
    
    def get(self, request, pk, format=None):
        turf = Turf.objects.get(pk=pk)
        serializers = TurfSerializer(turf)
        return Response(serializers.data, status=status.HTTP_200_OK)
        