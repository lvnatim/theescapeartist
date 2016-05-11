from blog.models import Post
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    post = Post.objects.filter(draft=False).order_by("-datestamp")[:1]
    post = post[0]
    return render(request, 'home/home.html', {"post":post})

def homeslide(request, num):
    num = int(num)
    post = Post.objects.filter(draft=False).order_by("-datestamp")
    try:
        post = post[num]
    except:
        post = post[0]
    return render(request, 'home/home.html', {"post":post})
