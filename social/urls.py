from django.urls import path
from social import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('post/', views.Post.as_view(), name='post'),
    path('', views.Posts.as_view(), name="posts")

]