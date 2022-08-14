import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import is_valid_path
from .forms import UserUpdateForm,  ProfileUpdateForm


def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please log In.')
            return redirect('login')
    else:
        form = UserCreationForm() 
    return render(request, 'users/register.html', {'form': form})



def profile(request):
    if request.method == 'POST' :
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def create(request):
    
    context = {
        'posts': posts
    }
    return render(request, 'users/create.html', context)

posts = [
 {
    'Meeting_name': ' Events Planning',
    'Created_by': ' Suede',
    'Date': ' 12/08/2022',
    'Absentees': 'Jane, Ryan',
    'Topic': ' Girl Power Event',
    'Raised_by': ' Kathy',
    'Actions_required': ' Someone to manage the ontake of roles',
    'Actioned_by': ' Nancy',
    'Extra_info': ' No extra work will be needed after event has been planned ',
    'Date_of_completion': ' 15/08/2022'   
 },
 {
    'Created_by': 'Suede',
    'Date': '12/08/2022',
    'Absentees': 'jane' 'Ryan',
    'Topic': 'Girl Power Event',
    'Rasied_by': 'Kathy',
    'Actions_required': 'Someone to manage the ontake of roles',
    'Actioned_by': 'Nancy',
    'Extra_info': 'Not needed',
    'Date_of_completion': '15/08/2022'   
 },
 {
    'Created_by': 'Suede',
    'Date': '12/08/2022',
    'Absentees': 'jane' 'Ryan',
    'Topic': 'Girl Power Event',
    'Rasied_by': 'Kathy',
    'Actions_required': 'Someone to manage the ontake of roles',
    'Actioned_by': 'Nancy',
    'Extra_info': 'Not needed',
    'Date_of_completion': '15/08/2022'   
 }
]
   