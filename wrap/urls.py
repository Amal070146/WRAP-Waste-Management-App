from django.urls import path
from .views import PostList, PostDetail,home,dashboard

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/',dashboard,name='dashboard'),
    #  path('simple-api/', PostList.as_view(), name='post_list'),
    # path('simple-api/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]