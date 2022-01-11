from django.db import models
from django.db.models.base import Model
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
class PostDetailview(DetailView):
    model = Post