from django.shortcuts import render,get_object_or_404_
from django.http import HttpResponse
from .models import Blogs,Category

# Create your views here.

def index(request):
    category=Category.objects.all()
    # blog=
    compact={
        'category': category
    }
    return render(request,"index.html",compact)
def blog(request):
    return render(request,'blog.html')
def category(request):
    return render(request,"category.html")
def contact(request):
    return render(request,"contact.html")
def single(request,pk):
    blog=get_object_or_404_(Blogs,id=pk)    
    return render(request,"single.html")