from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.http import urlquote

# Create your models here.

class Category(models.Model):
    name = models.CharField("Name", max_length = 16)
    
    def __unicode__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class Tag(models.Model):
    name = models.CharField("Name", max_length = 16)
    permalink = models.SlugField("Link", max_length = 50, null = True)
    
    def __unicode__(self):
        return self.name

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'permalink']

class Article(models.Model):
    title = models.CharField("Title", max_length = 100)
    author = models.CharField("Author", max_length = 16)
    content = models.TextField("Content")
    createTime = models.DateTimeField("CreateTime")
    
    permalink = models.SlugField("Link", null = True)

    category = models.ForeignKey(Category, verbose_name = "Category")
    tags = models.ManyToManyField(Tag, verbose_name = "Tag", related_name = "articles")
    
    def __unicode__(self):
        return self.title + ' - ' + self.author

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'createTime', 'permalink', 'category']

class FriendLink(models.Model):
    name = models.CharField("Name", max_length = 16)
    link = models.URLField("Link")
    
    def __unicode__(self):
        return self.name

class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']

class SinglePage(models.Model):
    title = models.CharField("Title", max_length = 100)
    content = models.TextField("Content")
    permalink = models.SlugField("Permalink")

class SinglePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'permalink']
