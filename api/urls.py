from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v<int:version_id>', views.version, name='version'),
    path('v<int:version_id>/get-articles', views.getArticles, name='getArticles'),
    path('v<int:version_id>/get-article/<int:id>', views.get_article_by_id, name='id'),
]