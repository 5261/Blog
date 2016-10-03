from django.shortcuts import render

from django.http import Http404
from .forms import CommentForm

# Create your views here.

from .models import Article, Comment, Tag, FriendLink

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
    
    if request.method == "GET":
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleanedData = form.cleaned_data
            cleanedData["article"] = article
            Comment.objects.create(**cleanedData)
    
    ctx = getBaseContent()
    ctx.update({
        "article" : article,
        "comments" : article.comment_set.all().order_by("-createTime"),
        "form" : form
    })
    
    return render(request, "article-detail.html", ctx)

def getArticlesByTag(request, tagName):
    
    tag = Tag.objects.get(name = tagName)
    articles = tag.articles.all().order_by("-createTime")
    
    ctx = getBaseContent()
    ctx.update({
        "articles" : articles
    })
    
    return render(request, "article-list.html", ctx)
