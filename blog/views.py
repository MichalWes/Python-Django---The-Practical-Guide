from django.shortcuts import render
from django.http import HttpResponse


def start_page(request):
    return HttpResponse("This is a startpage")


def posts(request):
    return HttpResponse("These are all posts")


def single_posts(request):
    return HttpResponse("This is the first post")
