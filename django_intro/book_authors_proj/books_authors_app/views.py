from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This is my new book")

# Create your views here.
