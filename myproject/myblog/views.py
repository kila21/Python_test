from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request,):
    template = 'myblog/index.html'
    return render(request, template)

def single_blog(request, blog_id):
    template = 'myblog/single_blog.html'
    item = Blog.objects.get(pk=blog_id)
    if(item):
        context = {'blog': item}
        return render(request, template, context)
    else:
        return render(request, 'Cannot Find Blog with This ID, %s.' % blog_id)