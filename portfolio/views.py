from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def home(request):
    projects= Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})

def all_blogs(request):
    blogs= Blog.objects.order_by('-date')[:5]
    return render(request,'portfolio/home.html',{'blogs':blogs})
