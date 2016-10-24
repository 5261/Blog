from django.shortcuts import render

from django.http import Http404

# Create your views here.

from .models import Article, Tag, FriendLink

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

def getDetail(request, articleId):
    try:
        article = Article.objects.get(id = articleId)
    except Article.DoesNotExist:
        return Http404
    
    ctx = getBaseContent()
    ctx.update({
        "article" : article,
    })
    
    return render(request, "article-detail.html", ctx)

def getArticlesByTag(request, tagName):
    try:
        tag = Tag.objects.get(name = tagName)
    except Tag.DoesNotExist:
        return Http404
    
    articles = tag.articles.all().order_by("-createTime")
    
    ctx = getBaseContent()
    ctx.update({
        "tag" : tag, 
        "articles" : articles
    })
    
    return render(request, "article-list-of-oneTag.html", ctx)
