from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['name', 'post', 'cover']


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'email', 'password']

class CommentForms(forms.ModelForm):

    class Meta:
        model=Comment
        fields=['comment', 'name', 'email']


