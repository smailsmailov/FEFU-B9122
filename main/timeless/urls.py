from django.urls import path

from .views import *

urlpatterns = [
    path('test/', TimelessAPIView.as_view()),
    path('data/', DataAPIView.as_view()),
]

