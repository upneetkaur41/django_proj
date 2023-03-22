from django.contrib import admin
from .models import Blog
# # Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title']

admin.site.register(Blog)