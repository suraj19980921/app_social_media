from social.models import Post
from django.urls import path
from social import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('post/', views.Post.as_view(), name='post'),
    path('post/<int:pk>/like/', views.PostLike.as_view(), name="like"),
     path('post/<int:pk>/comment/', views.PostComment.as_view(), name="comment"),
    path('', views.Posts.as_view(), name="posts"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)