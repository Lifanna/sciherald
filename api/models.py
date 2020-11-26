from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Source(models.Model):
    name = models.CharField("Название источника", max_length = 100, unique=True)

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateTimeField(null = True, blank = True)
    parsed_date = models.DateTimeField(null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    original_link = models.CharField("Источник статьи", max_length=255, null=False, blank=False, default="")

class Image(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    path = models.ImageField("Изображение", upload_to="articles_images", blank=True, null=True)
    original_path = models.TextField("Исходный путь изображения")
    position = models.IntegerField("Порядок")
