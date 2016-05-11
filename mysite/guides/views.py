from django.shortcuts import render

# Create your views here.
def guides(request):
    return render(request, 'guides/guides.html')
