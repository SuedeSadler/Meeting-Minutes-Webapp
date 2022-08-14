from .models import Post, Topics
from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Row, Column)




class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Date', 'Author', 'Atendees']
       
            
class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['Topic', 'Title', 'Raised_by', 'Actions', 'Actioned_by', 'Subsequent_info', 'Date_of_completion']
       

     