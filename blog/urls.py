from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page),
    path("posts", views.posts),
    path("posts<slug>", views.single_post)
]
