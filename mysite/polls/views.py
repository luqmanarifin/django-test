from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request, id):
    print request.method
    return HttpResponse("hello " + str(id))

def likes(request, id):
    print request.method
    return HttpResponse("likes " + str(id))