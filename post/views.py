from django.shortcuts import render
from post.models import Post
from django.views.generic import ListView
 
# Create your views here.

class PostListView(ListView):
    model=Post
    template_name="Home.html"
    context_object_name='posts'
