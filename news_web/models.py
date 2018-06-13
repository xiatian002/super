from __future__ import unicode_literals
from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-

from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.urls import reverse
from mdeditor.fields import MDTextField
#from django_markdown.models import MarkdownField


@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')

    nav_display = models.BooleanField('显示导航',default=False)
    home_display = models.BooleanField('显示首页',default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 排序
    def get_absolute_url(self):
        return reverse('column',args=(self.slug,))


@python_2_unicode_compatible
class Article(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属栏目')

    title = models.CharField('标题', max_length=256)
    slug = models.CharField('网址', max_length=256, db_index=True)

    news_author = models.ForeignKey('auth.User',related_name='news_author', blank=True, null=True,on_delete=models.CASCADE, verbose_name='作者')
    content = models.TextField('内容', default='', blank=True)
    #content = UEditorField('内容',height=300,width=1000,default=u'',blank=True,imagePath="uploads/images/",toolbars='besttome',filePath='uploads/files/') 
    #content = MarkdownField()
    #content = MDTextField('内容',default=u'',blank=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻稿'
        verbose_name_plural = '新闻稿'

    def get_absolute_url(self):
        return reverse('article',args=(self.pk,self.slug))
