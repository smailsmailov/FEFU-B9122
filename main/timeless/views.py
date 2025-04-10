from django.shortcuts import render


def test_view(request):
    context = {
        "test" : "test"
    }
    if ( request.method == "POST" ):
        context['req_post'] = request.POST['main_input']
        return render(request ,"index/index.html",context )
    if ( request.method == "GET"):
        context = {
                "name" : "NAME",
                "age" : "AGE",
                }
        return render(request ,"index/index.html",context )
