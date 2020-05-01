from django.shortcuts import render, redirect
def index(request):
    return render(request, 'form.html')

def process(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'language': request.POST['language'],
            'location': request.POST['location']
        }
        return render(request, 'results.html', context)
    return render(request, 'results.html')
        

# Create your views here.
