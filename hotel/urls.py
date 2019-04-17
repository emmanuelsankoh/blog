from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

app_name = 'hotel'

urlpatterns = [
    path('logout', views.logout_user, name='logout'),
    path('login', views.signin, name='login'),
    path('signup', views.signup, name='signup'),
    path('', views.PostListView.as_view(), name='index'),
    path('add-post', views.create_post, name='add-post'),
    path('<int:pk>/update-post', views.PostUpdateView.as_view(), name='post-update'),
    path('(?P<post_id>[0-9]+)/delete-post', views.post_delete, name='post-delete'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='comment'),
    path('(?P<post_id>[0-9]+)/new-comment', views.create_comment, name='new-comment'),





]