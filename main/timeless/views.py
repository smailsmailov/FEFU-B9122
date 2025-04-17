from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TimelessAPIView(APIView):

    def get(self, request, *args, **kwarrgs ):
        return Response("123", status = status.HTTP_200_OK)

    def post(self, request, *args, **kwarrgs ):
        data = request.data
        return Response(data['message'], status = status.HTTP_200_OK)
