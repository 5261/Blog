from django.contrib import admin

# Register your models here.

from .models import Category, Tag, Article, Comment

admin.site.register([Category, Tag, Article, Comment])
