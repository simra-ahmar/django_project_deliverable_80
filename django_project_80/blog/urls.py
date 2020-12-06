from django.urls import path
from . import views
from .views import PostListView, PostDetailView
from .views import  PostListView1, PostDetailView1
from customers.views import registration_view, login_view, logout_view


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('login/', login_view, name='customers-login'),
    path('restaurant/', PostListView.as_view(), name='blog-restaurants'),
    path('restaurantdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('restaurant1/',views.restaurants1,name='blog-restaurants1')
    path('restaurant1/',PostListView1.as_view(),name='blog-restaurants1'),
    path('restaurant1detail/<int:pk>/', PostDetailView1.as_view(), name='rest-detail'),
    path('menu/', views.menu, name='blog-menu'),
    path('menuO/', views.menuO, name='blog-menuO'),
    path('menuH/', views.menuH, name='blog-menuH'),
    path('menuS/', views.menuS, name='blog-menuS'),
    path('menuK/', views.menuK, name='blog-menuK'),
    path('menuD/', views.menuD, name='blog-menuD'),
    path('menuI/', views.menuI, name='blog-menuI'),
    path('logout/', logout_view, name='customers-logout'),
    #path('restaurant/', views.restaurants, name='blog-restaurants'),
    
    path('menuboot/', views.menuboot, name='blog-menubootstrap')



]
