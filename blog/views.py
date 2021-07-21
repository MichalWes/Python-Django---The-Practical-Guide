from django.shortcuts import render
from django.http import HttpResponse


def start_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return HttpResponse("These are all posts")


def single_post(request):
    return HttpResponse("This is the first post")
