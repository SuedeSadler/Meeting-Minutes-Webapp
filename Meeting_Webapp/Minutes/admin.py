from django.contrib import admin
from .models import Post
from .models import Topics

admin.site.register(Post)
admin.site.register(Topics)

