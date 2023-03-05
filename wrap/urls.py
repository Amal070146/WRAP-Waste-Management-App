from django.urls import path
from .views import home,dashboard,bin,bookings,rewards,news,redeem,pickupsuccess,notifications,support,settings,logout,track,profile,login,dropoff,pickup,report,signup

urlpatterns = [
    path('',login,name='login'),
    path('home/', home, name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    path('bookings/',bookings,name='bookings'),
    path('rewards/',rewards,name='rewards'),
    path('news/',news,name='news'),
    path('redeem/',redeem,name='redeem'),
    path('notifications/',notifications,name='notifications'),
    path('support/',support,name='support'),
    path('settings/',settings,name='settings'),
    path('logout/',logout,name='logout'),
    path('track/',track,name='track'),
    path('profile/',profile,name='profile'),
    path('signup/',signup,name='signup'),
    path('report/',report,name='report'),
    path('pickup/',pickup,name='pickup'),
    path('dropoff/',dropoff,name='dropoff'),
    path('bin/',bin,name='bin'),
    path('pickupsuccess/',pickupsuccess,name='pickupsuccess')
         


    #  path('simple-api/', PostList.as_view(), name='post_list'),
    # path('simple-api/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]