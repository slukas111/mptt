from django.shortcuts import render
from .models import Data


# Create your views here.

def index(request):
    html = 'index.html'
    data = Data.objects.all()
    return render(request, html, {'data': data})