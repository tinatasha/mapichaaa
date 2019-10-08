# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image, Location, Category
# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images':images})