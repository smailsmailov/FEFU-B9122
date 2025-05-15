from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
def get_csrf_token(request):
    token = get_token(request)
    return Response({"csrfToken": token})


@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
def test(request):
    return Response({"test": 123})


@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def test_1(request):
    # request.POST['key']
    name = request.data.get("name", "default value")
    return Response({"name": name})


@api_view(["GET"])
@authentication_classes([])
@permission_classes([IsAuthenticated])
def test_2(request):
    return Response({"test": 123})
