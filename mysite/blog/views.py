from .models import Post
from django.shortcuts import render

# Create your views here.
def blog(request):
    firstpost = Post.objects.filter(draft=False).order_by("-datestamp")[0]
    posts = Post.objects.filter(draft=False).order_by("-datestamp")[1:]
    return render(request, 'blog/blog.html', {"firstpost":firstpost, "posts":posts})
