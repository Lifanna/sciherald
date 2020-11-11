from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v<int:version_id>', views.version, name='version'),
    path('v<int:version_id>/articles', views.getArticles, name='getArticles'),
    path('v<int:version_id>/article/<int:id>', views.get_article_by_id, name='getArticleById'),
    path('v<int:version_id>/category/<int:id>', views.get_article_by_category, name="getArticleByCategory")
]