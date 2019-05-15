from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Lyubov',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 13, 2019'
     },
    {
        'author': 'Lyubov',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 14, 2019'
    },
    {
        'author': 'Maria',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'May 15, 2019'
    },
]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  #the last variable is the context dictionary to be passed to the about template