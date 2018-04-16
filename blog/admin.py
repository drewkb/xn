from django.contrib import admin
from .models import Post, Category, Page
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'


class PageAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'


admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category)

