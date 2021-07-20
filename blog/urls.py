from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page),
    path("posts", views.all_posts),
    path("my_first_post", views.first_post)
]
