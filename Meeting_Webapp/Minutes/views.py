from turtle import title
from urllib import request
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post, Topics
from users.models import User
from Minutes.models import Post, Topics
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostsForm, TopicsForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    logged_in_user_posts = Post.objects.all()
    return render(request, 'Minutes/home.html', {'posts': logged_in_user_posts})

def My_Meetings(request):
    logged_in_user_posts = Post.objects.filter(Author=request.user)
    return render(request, 'Minutes/My_Meetings.html', {'posts': logged_in_user_posts})

class PostListView(ListView):
    model = Post
    template_name = 'Minutes/My_Meetings.html'
    context_object_name = 'posts'
    ordering = ['-Date']
    
    def My_Meetings(request):
        logged_in_user_posts = Post.objects.filter(Author=request.user)
        return render(request, 'Minutes/My_Meetings.html', {'posts': logged_in_user_posts})
   
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'Minutes/post_detail.html'
    context_object_name = 'posts'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'Minutes/post_forms.html'
    fields = ['Title', 'Date', 'Atendees']
    
    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("topic-create")
    


class TopicCreateView(CreateView):
    model = Topics
    template_name = 'Minutes/Topic_forms.html'
    fields = ['Topic', 'Title', 'Raised_by', 'Actions', 'Actioned_by', 'Subsequent_info', 'Date_of_completion']
    success_message = 'Topic successfully created'
    def form_valid(self, form):
        # post =  Post.objects.filter(Title='Mad Day')
        # form.instance.Topic = post
        return super().form_valid(form)
    
    def get_success_url(self):
        if 'add_text' in self.request.POST:
            url = reverse("topic-create")
        else:
            url = reverse('minutes-My_Meetings')
        return url
        #return reverse("topic-create")


def Login(request):
    return render(request, 'Minutes/Login.html')
    
# def CreateMinutes(request):
#    if request.method == 'POST':
#         P_form = PostsForm(request.POST, instance=request.user)
#         T_form = TopicsForm(request.POST, instance=request.user)
#         if P_form.is_valid() and T_form.is_valid():
#             P_form.save()
#             T_form.save()
#             messages.success(request, f'Your account has been updated')
#             return redirect('Minutes/post_forms.html')
#         else:
#             P_form = PostsForm(instance=request.user)
#             T_form = TopicsForm(instance=request.user)
#    context = {
#        'P_form': P_form,
#        'T_form': T_form,
#    }
#    return render(request, 'Minutes/post_forms.html', context=context) 
    

# Create your views here.



