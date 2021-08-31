from django.urls import path
from social import views

urlpatterns = [
    path('', views.Posts.as_view(), name="posts")

]