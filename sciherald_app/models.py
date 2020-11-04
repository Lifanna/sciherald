from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length = 100, unique=True)


class Article(models.Model):
    name = models.CharField("Название статьи", max_length = 100, unique=True)
    category = models.ForeignKey("sciherald_app.Category", on_delete=models.SET_NULL, null=True)
    content = models.TextField("Содержание статьи", null=False, blank=False)
    author = models.CharField("Автор статьи", max_length=100)
    date = models.DateField("Дата публикации статьи")
    parsed_date = models.DateField("Дата разбора с сайта")
    source = models.CharField("Источник статьи", max_length=255)


class Image(models.Model):
    article = models.ForeignKey("sciherald_app.Article", on_delete=models.CASCADE)
    path = models.ImageField("Изображение", upload_to="articles_images", blank=True, null=True)
    original_path = models.TextField("Исходный путь изображения")
    position = models.IntegerField("Порядок")
