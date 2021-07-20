from django.shortcuts import render
from django.http import HttpResponse


def start_page(request):
    return HttpResponse("This is a startpage")


def all_posts(request):
    return HttpResponse("These are all posts")


def first_post(request):
    return HttpResponse("This is the first post")
