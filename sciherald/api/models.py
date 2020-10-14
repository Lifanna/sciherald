from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    category = models.CharField(max_length=255)
    referer_url = models.CharField(max_length=255)