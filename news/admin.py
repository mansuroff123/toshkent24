from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at']
    list_filter = ['create_at', 'category']
    search_fields = ['title', 'category', 'description']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_display_links = ['name']
