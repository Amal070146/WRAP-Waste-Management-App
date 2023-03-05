from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Post, Users, Booking
import folium


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def bin(request):
    return render(request, 'dashboard/bin.html')

def pickup(request):
    if request.method == 'POST':
        wastetype = request.POST.get('wastetype')
        date = request.POST.get('date')
        address = request.POST.get('address')
        print(date)
        book = Booking(wastetype=wastetype, date=date, address=address)
        book.save()

    return render(request, 'dashboard/pickup.html')


def report(request):
    return render(request, 'dashboard/report.html')


def dropoff(request):
    return render(request, 'dashboard/dropoff.html', {'form': form})


def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})


def rewards(request):
    return render(request, 'rewards.html')


def news(request):
    return render(request, 'news.html')


def redeem(request):
    return render(request, 'redeem.html')


def notifications(request):
    return render(request, 'notifications.html')


def support(request):
    return render(request, 'support.html')


def settings(request):
    return render(request, 'settings.html')


def logout(request):
    return render(request, 'logout.html')


def track(request):
    m = folium.Map(location=[10.307897806699529,
                   76.33507993927475], zoom_start=12)
    folium.Marker(location=[10.527627837215208, 76.21445706825584], popup="<p>Waste picked up</p>",
                  tooltip="11 AM", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(location=[10.512665164588398, 76.25561768977308], popup="<p>Reached collection point</p>",
                  tooltip="04:03 PM", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(location=[10.380721708232917, 76.2974580261964], popup="<p>Sent to Infinite waste LLC</p>",
                  tooltip="05:59 PM", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(location=[10.307003287734428, 76.33404101823123], popup="<p>On the way</p>",
                  tooltip="Just now", icon=folium.Icon(color="green")).add_to(m)
    trail_coordinates = [
        (10.527627837215208, 76.21445706825584),
        (10.523402028044528, 76.21676339524682),
        (10.519703423024081, 76.23536899988589),
        (10.516517757310858, 76.23639896810602),
        (10.512243214395411, 76.24628360262749),
        (10.512665164588398, 76.25561768977308),
        (10.511230531485214, 76.25838572952064),
        (10.44553925741713, 76.25895097511498),
        (10.438250590627376, 76.26464509672473),
        (10.434547789578632, 76.26604183367157),
        (10.413445049777307, 76.27076760239916),
        (10.394643441226956, 76.28688595976858),
        (10.387101170763309, 76.28899028286708),
        (10.383513125885708, 76.29289557903502),
        (10.380721708232917, 76.2974580261964),
        (10.371372889255452, 76.30409791447754),
        (10.370526874778777, 76.30986345834272),
        (10.371289720024908, 76.30407888007696),
        (10.370635399487753, 76.30944329789006),
        (10.367757892786981, 76.31390110718998),
        (10.357267374074375, 76.31662623143903),
        (10.351337316076425, 76.31821067557871),
        (10.34830617592037, 76.32067779967979),
        (10.341336158809888, 76.3223738294376),
        (10.337283183792525, 76.32153698025876),
        (10.32652276578376, 76.32295778284612),
        (10.31912449146524, 76.32680047441302),
        (10.311481803371343, 76.3310774898666),
        (10.307003287734428, 76.33404101823123)

    ]
    folium.PolyLine(trail_coordinates, tooltip="Coast",color="darkred").add_to(m)
    m = m._repr_html_()
    return render(request, 'track.html', { "m": m})


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == "POST":

        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(
                    username=request.POST['username'], email=request.POST['email'])
                user.save()
                return render(request, 'login.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                auth.login(request, user)
                user.save()
                return redirect('home')

        else:
            return render(request, 'login.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


