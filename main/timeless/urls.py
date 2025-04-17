from django.urls import path

from .views import *

urlpatterns = [
    path('test/', TimelessAPIView.as_view()),
]

