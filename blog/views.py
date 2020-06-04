from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.return request
def all_blogs(request):
    blogs= Blog.objects.order_by('-date')
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blog= get_object_or_404(Blog,pk=blog_id)# pk is primary key for the objects
    return render(request,'blog/detail.html',{'blog':blog})
    
