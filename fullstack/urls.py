from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('api/user', views.UserList.as_view()),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh')
]