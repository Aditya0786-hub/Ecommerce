from django.urls import path
from .views import TestApi

urlpatterns = [
    path('test/',TestApi.as_view(),name='test-api')
]
