from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog, Author

# Create your views here.


def home(request):
    context = {'name': 'Dipesh'}
    return render(request, 'blogs/home.html', context=context)


def post(request):
    return render(request, 'blogs/home.html')


def list_post(request):
    # return list
    data = Blog.objects.all()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'blogs/view.html', context=context)
