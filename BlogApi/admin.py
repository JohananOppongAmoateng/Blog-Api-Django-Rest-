from django.contrib import admin

# Register your models here.
from .models import Post,Comments

admin.site.register(Post)
admin.site.register(Comments)