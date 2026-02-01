from django.urls import path
from .views import RegisterApi,LoginApi,LogoutAPI

urlpatterns = [
    path('register/',RegisterApi.as_view(),name='register'),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout")
]
