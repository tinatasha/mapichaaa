# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(blank=True)
    image_name = models.CharField(max_length=200)
    image_description = models.TextField(max_length=600)
    image_location = models.CharField(max_length=200)
    image_category = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.image_name
    
    @classmethod
    def search_by_image_category(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images
    
class Location(models.Model):
    location = models.CharField(max_length=200)
    
    
class Category(models.Model):
    category = models.CharField(max_length=200)
    
    