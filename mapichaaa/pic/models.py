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
    
    def __str__(self):
        return self.image_name
    
    
class Location(models.Model):
    location = models.CharField(max_length=200)
    
    
class Category(models.Model):
    category = models.CharField(max_length=200)
    
    