from django.shortcuts import render
from django.http import JsonResponse

from .models import TestModel

def test_view(request):
    context = {
        "test" : "test"
    }
    if ( request.method == "POST" ):
        context['req_post'] = request.POST['main_input']
        return render(request ,"index/index.html",context )
    if ( request.method == "GET"):
        return render(request ,"index/index.html",context )
