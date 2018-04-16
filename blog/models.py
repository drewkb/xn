# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta


class Category(models.Model):

    title = models.CharField(max_length=150, verbose_name='Категория')
    logo = models.ImageField(upload_to='logo/', blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    def get_default_date():
        return timezone.now()+timedelta(days=7)

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name='Что? (до 150 сиволов)')
    categories = models.ManyToManyField(Category)
    text = models.TextField(verbose_name='Описание')
    begin = models.DateField(default=timezone.now, verbose_name='Когда начнется?')
    end = models.DateField(default=get_default_date, verbose_name='Когда закончится?')
    date = models.DateTimeField(auto_now=True)
    best = models.BooleanField(default=False, verbose_name='Лучшее')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])


class Page(models.Model):
    
    slug = models.SlugField()
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title









