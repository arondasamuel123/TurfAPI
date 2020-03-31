from rest_framework import serializers
from .models import User,Turf, Booking, Tournament, Schedule
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
class TurfSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    class Meta:
        model = Turf
        fields = ('id','turf_name', 'turf_location', 'price', 'user')
        
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    
    turf = serializers.PrimaryKeyRelatedField(
        queryset=Turf.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    class Meta:
        model = Booking
        fields = ('id', 'players', 'time', 'date', 'status', 'user','turf')

class TournamentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    
    turf = serializers.PrimaryKeyRelatedField(
        queryset=Turf.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    class Meta:
        model = Tournament
        fields = ('id', 'tournament_name','tournament_date','tournament_prize', 'tournament_poster', 'user','turf')


class ScheduleSerializer(serializers.ModelSerializer):
    turf = serializers.PrimaryKeyRelatedField(
        queryset=Turf.objects.all(),
        required=False,
        allow_null=True,
        default=None
    )
    turf_s = TurfSerializer
    class Meta:
        model = Schedule
        fields =('id', 'time_slot_one', 'time_slot_two', 'time_slot_three', 'day', 'turf')
    
    

        
    