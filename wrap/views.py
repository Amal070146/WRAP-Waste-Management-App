from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

def home(request):
    form = PostForm()
    return render(request, 'home.html', {'form': form})

def dashboard(request):
    form = PostForm()
    return render(request, 'dashboard.html', {'form': form})

def bookings(request):
    form = PostForm()
    return render(request, 'bookings.html', {'form': form})

def rewards(request):
    form = PostForm()
    return render(request, 'rewards.html', {'form': form})

def news(request):
    form = PostForm()
    return render(request, 'news.html', {'form': form})

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer