from django.contrib import admin

from .models import Comment, Post

"""Manage the Post model in the Django admin interface."""


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date', 'author')
    list_filter = ('status', 'date')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date'
    ordering = ('status', 'date')
    readonly_fields = ('image',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
