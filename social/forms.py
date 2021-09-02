from django import forms
from django.forms import fields
from social import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('content','image')

class PostComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']
