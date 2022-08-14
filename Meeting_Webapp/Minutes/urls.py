from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, TopicCreateView
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('My_Meetings', PostListView.as_view(), name='minutes-My_Meetings'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('topic/new/', TopicCreateView.as_view(), name='topic-create'),
    path('', views.home, name='minutes-home'),
    path('My_Meetings', views.My_Meetings, name='minutes-My_Meetings'),
    path('Login', views.Login, name='minutes-Login'),
]

urlpatterns += staticfiles_urlpatterns()