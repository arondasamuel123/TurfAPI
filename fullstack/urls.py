from . import views
from django.urls import path


urlpatterns = [
    path('api/user', views.UserList.as_view())
]