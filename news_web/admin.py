from django.contrib import admin
#from django_markdown.admin import MarkdownModelAdmin
# Register your models here.
from .models import Column,Article #two tables 
from mdeditor.widgets import MDEditorWidget

class ColumnAdmin(admin.ModelAdmin):
  list_display = ('name','slug','intro','nav_display','home_display')


class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title','slug','news_author','pub_date','update_time')
  #formfield_overrides={Article.TextField:{'widget':MDEditorWidget}}


admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)
#admin.site.register(MyModel, MarkdownModelAdmin)
