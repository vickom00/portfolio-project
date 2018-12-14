from django.shortcuts import render, get_object_or_404

from .models import Blog


def content(request):
    blog = Blog.objects
    return render(request, 'blog/content.html', {'blog': blog})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})