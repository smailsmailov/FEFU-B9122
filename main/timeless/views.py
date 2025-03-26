from django.shortcuts import render
from django.http import JsonResponse

from .models import TestModel


def test_view(request):
    # test_objects = TestModel.objects.filter().order_by('name')
    test_objects = TestModel.objects.all().order_by('create_at')


    # print(test_objects.name)

    for obj in test_objects:
        print(obj.create_at)


    data = {
        "status" : "ok",
        "message": "hello world",
    }
    return JsonResponse(data)
