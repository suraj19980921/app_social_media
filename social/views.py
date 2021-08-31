from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from social import models
from django.db.models import Q


# Create your views here.

class Posts(LoginRequiredMixin, ListView):
    context_object_name = "posts"
    template_name = "social/posts_list.html"
    login_url = "auth/login"

    def get_queryset(self):
        return models.Post.objects.filter(
            Q(user__person1 = self.request.user.pk) | Q(user__person2 = self.request.user.pk) &
            ~Q(user = self.request.user)
        )

class Home(LoginRequiredMixin, ListView):
    context_object_name = "posts"
    template_name = "social/home.html"
    login_url = "auth/login"

    def get_queryset(self):
        return models.Post.objects.filter(user = self.request.user)
        