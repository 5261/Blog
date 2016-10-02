from django.shortcuts import render

from django.http import Http404
from .forms import CommentForm

# Create your views here.

from .models import Article, Comment, Tag

def getArticles(request):
    ctx = {
        "articles" : Article.objects.all().order_by("-createTime"),
        "tags" : Tag.objects.all()
    }

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
            
    ctx = {
        "article" : article,
        "comments" : article.comment_set.all().order_by("-createTime"),
        "form" : form
    }
    
    return render(request, "article-detail.html", ctx)
