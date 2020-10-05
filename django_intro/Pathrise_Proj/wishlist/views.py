from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def wishes(request):
    context = {
        'wishes': Wish.objects.all()
    }
    return render(request, 'index.html', context)

def wish(request):
    if request.method == 'POST':
        new_wish = Wish.objects.create(name=request.POST['name'], job=request.POST['job'])
        print(new_wish)
    return redirect('/wishes')

def delete(request, id):
    destroyed = Wish.objects.get(id=id)
    destroyed.delete()
    return redirect('/wishes')

# Create your views here.
