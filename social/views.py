from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
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
        friendIds = [ friend.person2.id for friend in models.Friend.objects.filter(person1 = self.request.user)]
        friendIds = friendIds+[ friend.person1.id for friend in models.Friend.objects.filter(person2 = self.request.user)]
        return models.Post.objects.filter(user__in = friendIds).order_by('-created_at')
        

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
        post_form = forms.PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('/home/')

class PostLike(View):
    model = models.Post
    def post(self, request, pk):
        post = self.model.objects.get(pk=pk)
        models.Like.objects.create(post=post , user=request.user)
        return HttpResponse('Error')

class PostComment(View):
    model = models.Post
    form = forms.PostComment

    def post(self, request, pk):
        post = self.model.objects.get(pk = pk)
        form = self.form(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponse('ok')
        
        return HttpResponse('Error')