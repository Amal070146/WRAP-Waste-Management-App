from django.urls import path
from .views import PostList, PostDetail,home,dashboard,bookings,rewards,news,redeem,notifications,support,settings,logout,track,profile,login

urlpatterns = [
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
    path('',login,name='login'),

         


    #  path('simple-api/', PostList.as_view(), name='post_list'),
    # path('simple-api/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]