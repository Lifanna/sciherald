from django.http import HttpResponse
from django.shortcuts import render
from scrapy.crawler import CrawlerRunner
from parsers.habrparser.habrparser.spiders.habr_spider import HabrSpider
from scrapy.utils.project import get_project_settings

def index(request):
    return render(request, 'index.html')


def launch_spider(request):
    process = CrawlerRunner()
    process.crawl(HabrSpider)

    return HttpResponse()
