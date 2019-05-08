from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    search_fields = ['title', 'pub_date']
    list_filter = ['title', 'pub_date']
    ordering = ('pub_date',)
