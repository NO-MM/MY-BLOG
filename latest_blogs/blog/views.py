from django.shortcuts import render, redirect
from .models import BlogPost

# Create your views here.
def my_blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'my_blog_list.html', {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        BlogPost.objects.create(title=title, content=content, image=image)
        return redirect('my_blog_list')
    return render(request, 'blog_create.html')