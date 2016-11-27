from django.shortcuts import render

from django.http import Http404

# Create your views here.

from .models import Article, Tag, FriendLink, SinglePage
from django.conf import settings

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

def globalVariable(request):
    return {
        "SITE_URL" : settings.SITE_URL
    }

def getBaseContent():
    return {
        "tags" : Tag.objects.all(),
        "friendLinks" : FriendLink.objects.all()
    }

def getAllArticles(request):
    ctx = getBaseContent()
    ctx.update({
        "articles" : Article.objects.all().order_by("-createTime"),
    })

    return render(request, 'article-list.html', ctx)

def getArticleList(request, pageNum = 1):
    ctx = getBaseContent()
    
    allArticles = Article.objects.all().order_by("-createTime")
    pages = Paginator(allArticles, 10)

    try:
        articles = pages.page(pageNum)
    except PageNotAnInteger:
        articles = pages.page(1)
    except EmptyPage:
        articles = pages.page(pages.num_pages)
    
    ctx.update({
        "articles" : articles,
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

def getAboutPage(request):
    ctx = getBaseContent()
    ctx.update({
        "about" : SinglePage.objects.get(permalink = "about")
    })
    
    return render(request, "single-page/about.html", ctx)
