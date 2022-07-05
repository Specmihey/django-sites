import os
from django.db import models
from PIL import Image
from django.urls import reverse

# Модель раздела Направления
class directionCategory(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Направление')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='dir_cat_images/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dir_category', kwargs={'dir_cat_slug': self.slug})

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Направления'
        ordering = ['id', 'title']

#Модель страницы Направления
class directionCosmet(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='direction/%Y/%m/%d/', verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    dir_category = models.ForeignKey(directionCategory, on_delete=models.PROTECT, related_name='directions', verbose_name='Раздел направления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('direction', kwargs={'dir_slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи по Направлениям'
        ordering = ['-time_created', 'title']

#Модель галереи фотографий 
class directionImgGallery(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    image = models.ImageField(upload_to='directions_gallery/%Y/%m', verbose_name='Фото')
    album = models.ForeignKey(directionCosmet, on_delete=models.PROTECT, verbose_name='Направление')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея направления'
        ordering = ['-date_modified', 'title']

