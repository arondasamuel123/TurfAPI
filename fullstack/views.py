from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Turf, Booking, Tournament, Schedule, Join
from .serializers import UserSerializer,CustomTokenSerializer,TurfSerializer,BookingSerializer,TournamentSerializer, ScheduleSerializer,JoinSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .permissions import TurfOwner, TurfUser
from .email import send_booking_email, confirm_booking_email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


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
    permission_classes = (TurfOwner,IsAuthenticated)
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
        
    permission_classes = (TurfOwner,)
    def patch(self,request,pk, format=None):
        turf = Turf.objects.get(pk=pk)
        booking = Booking.objects.filter(turf_id=turf.id).first()
        user = User.objects.filter(id=booking.user_id).first()
        serializers = BookingSerializer(booking, data=request.data)
        if serializers.is_valid():
            serializers.save(user=booking.user, turf=turf)
            confirm_booking_email(user.username, user.email)
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserBookingView(APIView):
    permission_classes = (TurfUser,)
    def get(self, request,pk, format=None):
        user = User.objects.get(pk=pk)
        booking = Booking.objects.filter(user_id=user.id).first()
        serializers = BookingSerializer(booking)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        booking = Booking.objects.filter(user_id=user.id).first()
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TournamentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        tournaments = Tournament.objects.all()
        serializers = TournamentSerializer(tournaments, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
   
    
    permission_classes = (TurfOwner,)
    def get(self, request, pk, format=None):
        tournament = Tournament.objects.get(pk=pk)
        serializers = TournamentSerializer(tournament)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    
        
    def post(self,request,pk, format=None):
        turf = Turf.objects.get(pk=pk)
        users = User.objects.all()
        serializers = TournamentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=request.user, turf=turf)
            for user in users:
                if user.role_type=='TU':
                    mail_subject = "Tournament Notification"
                    sender = 'isproject.420@gmail.com'
                    message = render_to_string('email/tourna_email.txt', {"name": user.username, "turf":turf.turf_name})
                    html_content = render_to_string('email/tourna_email.html', {"name": user.username,"turf":turf.turf_name })
                    to_email = user.email
                    msg = EmailMultiAlternatives(mail_subject, message, sender, [to_email])
                    msg.attach_alternative(html_content, 'text/html')
                    msg.send()
                    return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        tournament = Tournament.objects.get(pk=pk)
        tournament.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ScheduleView(APIView):
    def get(self, request, pk, format=None):
        turf = Turf.objects.get(pk=pk)
        schedule = Schedule.objects.filter(turf_id=turf.id).first()
        serializers = ScheduleSerializer(schedule)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self,request,pk, format=None):
        turf = Turf.objects.get(pk=pk)
        serializers = ScheduleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(turf=turf)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk, format=None):
        turf = Turf.objects.get(pk=pk)
        schedule = Schedule.objects.filter(turf_id=turf.id).first()
        serializers = ScheduleSerializer(schedule,data=request.data)
        if serializers.is_valid():
            serializers.save(turf=turf)
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
class JoinView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        tournament = Tournament.objects.get(pk=pk)
        join = Join.objects.filter(tournament_id=tournament.id).first()
        serializers = JoinSerializer(join)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, format=None):
        tournament = Tournament.objects.get(pk=pk)
        serializers = JoinSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(tournament=tournament)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)        