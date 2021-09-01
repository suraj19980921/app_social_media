from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from social import models
from django.db.models import Q
from social import forms
from django.views import View


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
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['post_form'] = forms.PostForm()
        return data 

class Post(View):
    def post(self, request):
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('/home/')