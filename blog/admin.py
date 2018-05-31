from django.contrib import admin
from .models import Post, Category, Page
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
  
    summernote_fields = '__all__'
    list_display = ('title', 'date', 'author', 'begin', 'end')
    list_filter = ['date', 'begin', 'end']
    search_fields = ['title']
    fieldsets = [
        (None,               {'fields': ['author', 'title', 'best', 'begin', 'end']}),
        ('Описание. Не забывайте правила работы с картинками', {'fields': ['text']}),
    ]


class PageAdmin(SummernoteModelAdmin): 
 
    summernote_fields = '__all__'


admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category)

