from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField("Название категории", max_length = 100, unique=True)


class Source(models.Model):
    name = models.CharField("Название источника", max_length = 100, unique=True)


class Article(models.Model):
    name = models.CharField("Название статьи", max_length = 100, null=False, default="")
    category = models.ForeignKey("api.Category", on_delete=models.SET_NULL, null=True)
    content = models.TextField("Содержание статьи", null=False, blank=False)
    author = models.CharField("Автор статьи", max_length=100)
    date = models.DateField("Дата публикации статьи", null=True, blank=True)
    parsed_date = models.DateField("Дата разбора с сайта", null=True, blank=True)
    source = models.ForeignKey("api.Source", on_delete=models.SET_NULL, null=True)
    original_link = models.CharField("Источник статьи", max_length=255, null=False, blank=False, default="")


class Image(models.Model):
    article = models.ForeignKey("api.Article", on_delete=models.CASCADE)
    path = models.ImageField("Изображение", upload_to="articles_images", blank=True, null=True)
    original_path = models.TextField("Исходный путь изображения")
    position = models.IntegerField("Очередность изображения в тексте статьи", default=0)
