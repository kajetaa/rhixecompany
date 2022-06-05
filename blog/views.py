from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def indexblog(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ': ' + recent_post.content)