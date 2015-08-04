from django.db import models
from django.utils import timezone

class URLapp(models.Model):
	shorturl = models.URLField()
	httpstat = models.PositiveIntegerField()
	finaldestination = models.URLField()
	pagetitle = models.CharField(max_length=None)
