from django.shortcuts import render, redirect
from .models import Blog

from .forms import addBlogForm

# Create your views here.

def index(request,):
    template = 'myblog/index.html'
    list_length = len(Blog.objects.all())
    return render(request, template, {'blogs': list_length})

def single_blog(request, blog_id):
    template = 'myblog/single_blog.html'
    item = Blog.objects.get(pk=blog_id)
    if(item):
        context = {'blog': item}
        return render(request, template, context)
    else:
        return render(request, 'Cannot Find Blog with This ID, %s.' % blog_id)
    
def add_blog(request):
    if request.method == 'POST':
        form = addBlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = addBlogForm()

    return render(request, 'myblog/add_blog.html', {'form': form})
