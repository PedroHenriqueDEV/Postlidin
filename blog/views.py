from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    db = {}
    db['Post'] = Post.objects.all()

    return render(request,'blog/home.html',db)

def guia(request):
    return render(request,'blog/guia.html')

def eu(request):
    return render(request,'blog/eu.html')