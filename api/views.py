from django.http import JsonResponse, HttpResponse
from django.http import Http404
from django.shortcuts import render
from api.models import Article
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

    q1 = Article(
        id = 1,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q1.save()

    q2 = Article(
        id = 2,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q2.save()

    q3 = Article(
        id = 3,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q3.save()

    q4 = Article(
        id = 4,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q4.save()

    q5 = Article(
        id = 5,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q5.save()

    q6 = Article(
        id = 6,
        title = 'Здесь будет название статьи',
        content = 'Здесь будет очень длинный контент, который мы будем парсить с сайтов!',
        author = 'Фамилия Имя Отчество',
        publication_date = datetime.datetime(2020, 10, 12),
        category = 'Здесь будет категория статьи',
        referer_url = 'http://habr.com/all'
    )
    q6.save()

    data = json.dumps(list(Article.objects.values()), ensure_ascii=False, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type='application/json')
