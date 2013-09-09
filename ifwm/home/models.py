# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import default


class Urls(models.Model):
    id = models.AutoField(primary_key=True)
    urlhash = models.CharField(max_length=32L, unique=True)
    url = models.CharField(max_length=512L)
    status = models.IntegerField(default=0)
    date = models.IntegerField(default=0)
    class Meta:
        db_table = 'urls'

class Pages(models.Model):
    url =  models.OneToOneField(Urls,primary_key=True)
    images_total = models.IntegerField(default=0)
    images_ready = models.IntegerField(default=0)
    class Meta:
        db_table = 'pages'

class Images(models.Model):
    url = models.OneToOneField(Urls,primary_key=True)
    ext = models.CharField(max_length=8L)
    has_s = models.IntegerField(default=0)
    page = models.ManyToManyField(Pages)
    class Meta:
        db_table = 'images'
