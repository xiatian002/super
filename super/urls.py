"""super URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include#include 属于urls的模块
from django.conf import settings
from . import view
from news_web import views as news_web_views #导入news_web app中的views模块
from DjangoUeditor import urls as DjangoUeditor_urls
from django.conf.urls.static import static
from news_web import update_domain 
#import mdeditor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('domain/',update_domain.update_domain),
    url(r'^$',news_web_views.index,name="index"),
    url(r'^ueditor/',include(DjangoUeditor_urls)),#引用外部urls与引用admin不同需要嵌套在include方法中才可以使用
    url(r'^column/(?P<column_slug>[^/]+)/$',news_web_views.column_detail,name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',news_web_views.article_detail,name='article'),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'markdown/', include('django_markdown.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
  MEDIA_ROOT = os.path.join(settings.BASE_DIR,'media')
  urlpatterns += static(
    settings.MEDIA_URL,document_root=settings.MEDIA_ROOT )
