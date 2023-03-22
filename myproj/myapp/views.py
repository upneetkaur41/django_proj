
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,Http404
from myapp.forms import BlogForm
from myapp.models import Blog
# Create your views here.

def create_blog(request): 
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'create.html', {'form': form})
    
def list_blogs(request):
    blog = Blog.objects.all()
    return render(request,'list.html', {'blog': blog})

def delete_blog(request,**kwargs):
    if pk:=kwargs.get('pk'):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
    blog = Blog.objects.all()
    return render(request,'list.html', {'blog': blog})

def update_blog(request, **kwargs):
    # context = {}
    form = BlogForm()
    if request.method == 'POST':
        if pk:= kwargs.get('pk'):
            obj = BlogForm.objects.get(pk=pk)
            form = BlogForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # context['form'] = form
                HttpResponseRedirect('/blog/list')
    return render(request, 'update.html' ,{'form':form})
