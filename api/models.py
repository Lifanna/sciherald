from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    parsed_date = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    source = models.CharField(max_length=255)

class Image(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    path = models.ImageField("Изображение", upload_to="articles_images", blank=True, null=True)
    original_path = models.TextField("Исходный путь изображения")
    position = models.IntegerField("Порядок")

class Article(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     img = models.ImageField(upload_to='/article', 
                      height_field=100, width_field=100)