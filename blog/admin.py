from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Comment, Post #, Image

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
#admin.site.register(Image)

# admin.site.register(Post)
# admin.site.register(Comment)
# admin.site.register(Category)
