from django.urls import path

from .views import *

urlpatterns = [
    path('test/', test_view),
]

