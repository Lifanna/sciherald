from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v<int:version_id>', views.version, name='version'),
    path('v<int:version_id>/articles', views.getArticles, name='getArticles'),
    path('v<int:version_id>/articles/<int:id>', views.getArticle, name='getArticleById'),
    path('v<int:version_id>/category/<int:category_id>', views.get_article_by_category, name="getArticleByCategory"),
    path('v<int:version_id>/categories', views.getCategories, name="getAllCategory"),
    path('v<int:version_id>/images/<int:article_id>', views.get_images_by_article, name="getImagesByArticle"),
]