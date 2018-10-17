from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Word(models.Model):
	name=models.CharField(max_length=200)
	tag=models.CharField(max_length=200)
