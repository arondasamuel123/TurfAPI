from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('api/user', views.UserList.as_view()),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/turf', views.TurfView.as_view()),
    path('api/v1/turfs',views.TurfList.as_view()),
    path('api/v1/turf/<int:pk>', views.SingleTurf.as_view()),
    path('api/v1/booking/<int:pk>', views.BookingView.as_view()),
    path('api/v1/view/<int:pk>', views.UserBookingView.as_view()),
    path('api/v1/tournaments', views.AllTournamentsView.as_view()),
    path('api/v1/tourna/<int:pk>', views.TournamentView.as_view()),
    path('api/v1/tournament/<int:pk>', views.TournamentView.as_view()),
    path('api/v1/schedule/<int:pk>', views.ScheduleView.as_view()),
    path('api/v1/join/<int:pk>',views.JoinView.as_view())
    
    
]