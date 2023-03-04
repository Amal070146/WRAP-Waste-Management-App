from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
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

def pickup(request):
    form = PostForm()
    return render(request, 'dashboard/pickup.html', {'form': form})

def report(request):
    form = PostForm()
    return render(request, 'dashboard/report.html', {'form': form})

def dropoff(request):
    form = PostForm()
    return render(request, 'dashboard/dropoff.html', {'form': form})

def bookings(request):
    form = PostForm()
    return render(request, 'bookings.html', {'form': form})

def rewards(request):
    form = PostForm()
    return render(request, 'rewards.html', {'form': form})

def news(request):
    form = PostForm()
    return render(request, 'news.html', {'form': form})

def redeem(request):
    form = PostForm()
    return render(request, 'redeem.html', {'form': form})

def notifications(request):
    form = PostForm()
    return render(request, 'notifications.html', {'form': form})

def support(request):
    form = PostForm()
    return render(request, 'support.html', {'form': form})

def settings(request):
    form = PostForm()
    return render(request, 'settings.html', {'form': form})

def logout(request):
    form = PostForm()
    return render(request, 'logout.html', {'form': form})

def track(request):
    form = PostForm()
    return render(request, 'track.html', {'form': form})

def profile(request):
    form = PostForm()
    return render(request, 'profile.html', {'form': form})

# def login(request):
#     form = PostForm()
#     return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'login.html', {'error':'Password does not match!'})
    else:
        return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer