from django.contrib import admin
from . models import post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'publish')
    
    list_display_links = ('title', 'author')
    ordering = ('-publish',)
    prepopulated_fields ={'slug': ('title',)}
    search_fields = ('title', 'body')
    
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets =()
    
    author = ('username',)


admin.site.register(post, PostAdmin)