from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

from django.shortcuts import render
from myapp.models import Flower

def index(request):
    flowers = Flower.objects.all()
    
    return render(request, 'myapp/index.html', {'flowers': flowers })