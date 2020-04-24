from django.shortcuts import render


# Function Home
# handles traffic from blog

posts = [
    {'author': 'toreyo',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'datePosted': 'April 22, 2020'
    },
      {'author': 'toreyo',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'datePosted': 'April 23, 2020'
    },

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
