from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """
    Create a view that will return a list of Posts
    that were published prior to 'now' and render
    them to the 'blogposts.html' template.
    """

def post_detail(request):
    """
    Create a view that returns a single Post object
    based on the Post ID (pk) and 
