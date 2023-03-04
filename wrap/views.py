from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from rest_framework import generics
from .models import Post,Users,Booking
from .serializers import PostSerializer

def home(request):
    form = PostForm()
    return render(request, 'home.html', {'form': form})

def dashboard(request):
    form = PostForm()
    return render(request, 'dashboard.html', {'form': form})

def pickup(request):
    if request.method=='POST':
        wastetype = request.POST.get('wastetype')
        date = request.POST.get('date')
        address = request.POST.get('address')
        print(date)
        book=Booking(wastetype=wastetype,date=date,address=address)
        book.save()

    return render(request, 'dashboard/pickup.html')

def report(request):
    form = PostForm()
    return render(request, 'dashboard/report.html', {'form': form})

def dropoff(request):
    form = PostForm()
    return render(request, 'dashboard/dropoff.html', {'form': form})

def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

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

def signup(request):
    if request.method == "POST":
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'],email = request.POST['email'])
                user.save()
                return render(request,'login.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email = request.POST['email'])
                auth.login(request,user)
                user.save()
                return redirect('home')
                
        else:
            return render (request,'login.html', {'error':'Password does not match!'})
    else:
        return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'],email = request.POST['email'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer