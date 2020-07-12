from django.shortcuts import render
from .models import Post



# Function Home
# handles traffic from blog



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
