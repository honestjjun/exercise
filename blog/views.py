from django.shortcuts import render

from .models import Blog


def main(request):
    posts = Blog.objects.all()
    return render(request, 'main.jinja', {'posts': posts})