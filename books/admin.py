from django.contrib import admin
from .models import Publisher, Author, Book


# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state_province', 'country', 'website']
    search_fields = ['name', 'website']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['salutation', 'name', 'email', 'headshot']
    search_fields = ['salutation', 'name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publisher', 'publication_date']
    search_fields = ['title', 'publisher', 'publication_date']
    list_filter = ('title', 'publisher',)
    ordering = ('publication_date', 'title',)
