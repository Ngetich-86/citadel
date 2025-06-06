from django.shortcuts import render
from django.http import HttpResponse

def server_status(request):
    return HttpResponse("Server is running smoothly!")

# Create your views here.
