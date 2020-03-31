from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Turf, Booking
from .serializers import UserSerializer,CustomTokenSerializer,TurfSerializer,BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .permissions import TurfOwner
from .email import send_booking_email, confirm_booking_email


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
    def put(self, request, pk, format=None):
        turf = Turf.objects.get(pk=pk)
        serializers = TurfSerializer(turf, data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        turf = Turf.objects.get(pk=pk)
        booking = Booking.objects.filter(turf_id=turf.id).first()
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request, pk, format=None):
        turf = Turf.objects.get(pk=pk)
        user = User.objects.filter(id=turf.user_id).first()
        serializers = BookingSerializer(data=request.data)
        
        if serializers.is_valid():
            serializers.save(user=request.user, turf=turf)
            send_booking_email(user.username, user.email)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    def put(self,request,pk, format=None):
        turf = Turf.objects.get(pk=pk)
        booking = Booking.objects.filter(turf_id=turf.id).first()
        user = User.objects.filter(id=booking.user_id).first()
        serializers = BookingSerializer(booking, data=request.data)
        if serializers.is_valid():
            serializers.save(user=booking.user, turf=turf)
            confirm_booking_email(user.username, user.email)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class UserBookingView(APIView):
#     def get(self, request,pk, format=None):
#         user = User.objects.get(pk=pk)
#         booking = Booking.objects.filter(user_id=user.id).first()
#         serializer
            
        
        
            
        
        