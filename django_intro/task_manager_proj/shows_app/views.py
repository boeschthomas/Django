from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def goback(request):
    return redirect('/shows')

def go_to_show(request):
    return render(request,'one_shows.html')

def new(request):
    return render(request, 'new.html')

def shows(request):
    context = {
        'all_shows': Shows.objects.all()
    }
    return render(request, 'shows.html', context)

def create_shows(request):
    if request.method == 'POST':
        new_shows = Shows.objects.create(shows=request.POST['shows'])
        print(new_shows)
        return redirect('/one_shows')
    return redirect('/')

def one_shows(request, id):
    context = {
        'viewed_shows':Shows.objects.get(id=id)
    }
    return render(request, 'one_shows.html', context)

def shows_edit_page(request, id):
    context = {
        'edit_shows': Shows.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def process_edit(request, id):
    if request.method == 'POST':
        str_id = str(id)
        edit_shows = Shows.objects.get(id=id)
        edit_shows.shows = request.POST['shows']
        edit_shows.save()
        return redirect(f'/shows/{str_id}')
    return redirect('/')

def delete_shows(request, id):
    shows = Shows.objects.get(id=id)
    shows.delete()
    return redirect('/shows')

# Create your views here.
