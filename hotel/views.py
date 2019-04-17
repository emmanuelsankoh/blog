from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, UpdateView, DetailView
from .forms import PostForm,UserForm, CommentForms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = "posts"

class PostDetailView(DetailView):
    model=Post


def create_comment(request, post_id):
    form=CommentForms(request.POST or None, request.FILES or None)
    post=get_object_or_404(Post, pk=post_id)
    if form.is_valid():
        for s in post.comment_set.all():
            if s.comment==form.cleaned_data.get('comment'):
                context={
                    'form':form,
                    'message':'You already added that comment'
                }
                return render(request, 'hotel/add-comment.html', context)
        comment=form.save(commit=False)
        comment.post=post
        comment.save()
        return render(request, 'hotel/add-comment.html', {'comment':comment})
    return render(request, 'hotel/add-comment.html', {'form':form})


def create_post(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post =Post.objects.filter(user=request.user)
        post=form.save(commit=False)
        post.cover=request.FILES['cover']
        post.user=request.user
        post.save()
        return render(request, 'hotel/post_list.html', {'post':post})
    return render(request, 'hotel/create_post.html', {'form':form})


class PostUpdateView(UpdateView):
    model=Post
    fields=['name', 'post', 'cover']
    template_name='hotel/create_post.html'



def post_delete( request,post_id):
    post=get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')

def signup(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=form.save(commit=False)
        user.set_password(password)
        user.save()
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('hotel:index')
    return render(request, 'registration/signup.html', {'form': form})



def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('hotel:index')
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    context={
        'message':'Hey you are Logged Out!'
    }
    return render(request, 'registration/login.html', context)