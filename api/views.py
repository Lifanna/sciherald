from django.http import JsonResponse, HttpResponse
from django.http import Http404
from django.shortcuts import render
from api.models import Article, Category
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import datetime
import json

from rest_framework import generics

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

def getArticles(request, version_id):
    if version_id != 1:
        raise Http404('Unknown version of api')

    objects = Article.objects.order_by('id')
    data = serializers.serialize('json', objects)

    print('OBJECCCCCTSSSSSSSSSSSSS     = = = = = ', objects)
    print('DATAAAAAAAAAAAAAAAAAAAAA     = = = = = ', data)

    return HttpResponse(data, content_type='application/json')


def get_article_by_id(request, version_id, id):

    objects = Article.objects.get(pk=id)
    data = serializers.serialize('json', [objects])

    print('OBJ     = = = = = ', objects)
    print('DAT     = = = = = ', data)

    return HttpResponse(data, content_type='application/json')

def get_article_by_category(request, version_id, id):
    categoryArticles = Article.objects.filter(category=id)

    data = serializers.serialize('json', categoryArticles)

    return HttpResponse(data, content_type='application/json')
