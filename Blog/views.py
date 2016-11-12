from django.shortcuts import render

from django.http import Http404

# Create your views here.

from .models import Article, Tag, FriendLink
from django.conf import settings

def globalVariable(request):
    return {
        "SITE_URL" : settings.SITE_URL
    }

def getBaseContent():
    return {
        "tags" : Tag.objects.all(),
        "friendLinks" : FriendLink.objects.all()
    }

def getArticles(request):
    ctx = getBaseContent()
    ctx.update({
        "articles" : Article.objects.all().order_by("-createTime"),
    })

    return render(request, 'article-list.html', ctx)

def getArchive(request):
    ctx = getBaseContent()
    ctx.update({
        "articles" : Article.objects.all().order_by("-createTime"),
    })
    
    return render(request, 'article-archive.html', ctx)

def getDetail(request, articleLink):
    try:
        article = Article.objects.get(permalink = articleLink)
    except Article.DoesNotExist:
        return Http404
    
    ctx = getBaseContent()
    ctx.update({
        "article" : article,
    })
    
    return render(request, "article-detail.html", ctx)

def getArticlesByTag(request, tagLink):
    try:
        tag = Tag.objects.get(permalink = tagLink)
    except Tag.DoesNotExist:
        return Http404
    
    articles = tag.articles.all().order_by("-createTime")
    
    ctx = getBaseContent()
    ctx.update({
        "tag" : tag, 
        "articles" : articles
    })
    
    return render(request, "article-list-of-oneTag.html", ctx)
