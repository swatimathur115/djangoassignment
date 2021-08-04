from django.contrib import admin
# # Register your models here.
from .models import Post,Category,Tag,CustomUser,Comment

class PostAdmin(admin.ModelAdmin):    
    list_display = ('title', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title']
    filter_horizontal =["tag"]

class CustomUserAdmin(admin.ModelAdmin):
    list_display =("username", "email")
    list_filter=['username']
    search_fields=['username']

class CategoryAdmin(admin.ModelAdmin):   
    search_fields=['category_name']
    list_filter=['category_name']

class TagAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_filter=['name']

class CommentAdmin(admin.ModelAdmin):
    list_display =("post","name","comment","created_date")
    list_filter=['post']
    search_fields=['post']

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment,CommentAdmin)

