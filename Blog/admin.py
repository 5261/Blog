from django.contrib import admin

# Register your models here.

from .models import Category, Tag, Article, FriendLink, SinglePage
from .models import CategoryAdmin, TagAdmin, ArticleAdmin, FriendLinkAdmin, SinglePageAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(FriendLink, FriendLinkAdmin)
admin.site.register(SinglePage, SinglePageAdmin)
