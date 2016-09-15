from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    name = models.CharField("Name", max_length = 16)

class Tag(models.Model):
    name = models.CharField("Name", max_length = 16)

class Article(models.Model):
    title = models.CharField("Title", max_length = 32)
    author = models.CharField("Author", max_length = 16)
    content = models.TextField("Content")
    createTime = models.DateTimeField("CreateTime", auto_now_add = True)

    category = models.ForeignKey(Category, verbose_name = "Category")
    tags = models.ManyToManyField(Tag, verbose_name = "Tag")
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "createTime")

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name = "Artile")

    name = models.CharField("Name", max_length = 16)
    email = models.EmailField("Email")
    content = models.CharField("Content", max_length = 140)

    createTime = models.DateTimeField("CreateTime", auto_now_add = True)
