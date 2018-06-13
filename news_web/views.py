from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Column,Article
from django.shortcuts import redirect

#def index(request):
 # return HttpResponse(u'欢迎观临自强新闻网站')

def column_detail(request, column_slug):
  column= Column.objects.get(slug=column_slug)
  return render(request,'news_web/column.html',{'column':column})#此处的目录结构为porject/app/templates/nets/templates跟index.html的所在目录不同
#  return HttpResponse('column slug:' + column_slug)

def article_detail(request,pk, article_slug):
#  article = Article.objects.get(slug=atricle_slug)#一个网址可以对应多个文章的bug
#  article = Article.objects.filter(slug=article_slug)[0]#有多个网址对应时将只显示第一个,临时解决方案
  article = Article.objects.get(pk=pk)

  if article_slug != article.slug:
    return redirect(article,permanent=True)

  return render(request,'news_web/article.html',{'article':article})

def index(request):
  columns=Column.objects.all()
  return render(request,'index.html',{'columns':columns})#此处的index.html需要放在项目的templates目录下不能放在app的templates下
  home_display_columns=Column.objects.filter(home_display=True)
  nav_display_columns=Column.objects.filter(nav_display=True)
  
  return render(request,'index.html',{
    'home_display_columns':home_display_columns,
    'nav_display_columns':nav_display_columns,
  })
