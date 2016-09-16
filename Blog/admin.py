from django.contrib import admin

# Register your models here.

from .models import Category, Tag, Article, Comment
from .models import CategoryAdmin, TagAdmin, ArticleAdmin, CommentAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
