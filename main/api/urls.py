from django.urls import path

from .views import *

urlpatterns = [
    path("get_csrf_token/", get_csrf_token),
    path("test/", test),
    path("test_1/", test_1),
    path("test_2/", test_2),
]
