from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def rodrigo(request):
    return HttpResponse("Hello Rodrigo")


def david(rquest):
    return HttpResponse("Hello David")


def greet(request, name):
    return render(request, "hello/greet.html" , {
        "name": name.capitalize()
    })
    # HttpResponse(f"Hello {name.capitalize( )}!")