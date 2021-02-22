from django.urls import path
from .views import matcher

urlpatterns = [
    path('', matcher, name='matcher')
]