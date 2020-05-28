from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def add_book(request):
    if request.method == "POST":
    return render(request, 'add_book.html'),

def one_book (request):
    return render(request, 'one_book.html')




