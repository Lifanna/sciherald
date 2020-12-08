from django.http import JsonResponse, HttpResponse
from django.http import Http404
from django.shortcuts import render
from api.models import Article, Category, Image
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import datetime
import json

from rest_framework import generics

from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    info = {
        '/api': 'Main page of Sciherald Backend API',
        '/v1': 'Version of api',
        '/v1/get-articles': 'Method to get all articles',
    }
    context = {'info': info}
    return render(request, 'api/index.html', context)

def version(request, version_id):
    if version_id != 1:
        raise Http404('Unknown version of api')
    
    return JsonResponse({
        'info': 'version of api is v1'
    })


@api_view(['GET'])
def getArticles(request, version_id):
    print('fffffffffffffffffffffffffffff')
    serializer = serializers.ArticleSerializer(Article.objects.all()[:100], many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getCategories(request, version_id):
    serializer = serializers.CategorySerializer(Category.objects.all(), many=True)
    
    return Response(serializer.data)
    

@api_view(['GET'])
def getArticle(request, version_id, id):
    article = get_object_or_404(Article, pk=id)
    
    # Article.objects.filter(source_id=3).first()
    serializer = serializers.ArticleSerializer(article)

    return Response(serializer.data)

@api_view(["GET"])
def get_article_by_category(request, version_id, category_id):
    article = Article.objects.filter(category = category_id)[:10]
    print('FFFFFFFFFFFFFFFFFFFFFFFFFFFUCK')
    # Article.objects.filter(source_id=3).first()
    serializer = serializers.ArticleSerializer(article, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def get_images_by_article(request, version_id, article_id):
    images = Image.objects.filter(article_id = article_id)
    
    # Article.objects.filter(source_id=3).first()
    serializer = serializers.ImageSerializer(images, many=True)

    return Response(serializer.data)
