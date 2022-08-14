from email.mime import image
from email.policy import default
from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateField(default= timezone.now)
    Atendees = models.CharField(max_length=100)
   
    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    
    
    
    
class Topics(models.Model):
    Topic = models.ForeignKey(Post, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100 )
    Raised_by = models.CharField(max_length=100)
    Actions = models.TextField()
    Actioned_by = models.CharField(max_length=100)
    Subsequent_info = models.TextField()
    Date_of_completion = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.Title    
    
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})