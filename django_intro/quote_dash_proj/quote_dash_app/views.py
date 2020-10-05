from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import * 

def index(request):
    return render(request, 'index.html')

def quotes(request):
    if 'name' in request.session:
        return render(request, 'quotes.html')
    return redirect('/')

def quotes(request):
    context = {
        'all_posts': Quote_Posts.objects.all()
    }
    return render(request, 'quotes.html', context)
    

def register(request):
    print(request.POST)
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=hashed_password)
    print(new_user, "This is my new user!")
    request.session['name'] = new_user.first_name
    return redirect('/quotes')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user)>0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            print(logged_user, "logged user was signed in!")
            request.session['name'] = logged_user.first_name
            return redirect('/quotes')

    return redirect('/')

def create_quote(request):
    if request.method == 'POST':
        new_quote = Quote_Posts.objects.create(quote=request.POST['contents'], poster=User.objects.get(id=request.session['id']))
        print(new_quote)
        request.session['name'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/quote')
    return redirect('/')

def like_message(request, id):
    liked_message = Quote_Posts.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.likes.add(user_liking)
    return redirect('/quote')

def logout(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
