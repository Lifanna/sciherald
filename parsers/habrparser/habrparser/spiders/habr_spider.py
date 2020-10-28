import scrapy, w3lib
from ..items import HabrparserItem
from datetime import datetime

class HabrSpider(scrapy.Spider):
    name = "habr"
    main_url = 'https://habr.com/ru/'

    def start_requests(self):
        urls = [
            'https://habr.com/ru/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url

        categories = response.css("ul.nav-links > li")
        category_name = response.css("ul.nav-links > li")

        i = 0
        for category in response.css("ul.nav-links > li"):
            i += 1
            if i == 1: 
                continue
            elif i > 2:
                break

            category_link = category.css('a::attr(href)').extract_first()
            category_name = category.css('a::text').extract_first()

            item = HabrparserItem()
            item['category'] = category_name
            
            request = scrapy.Request(url=category_link, callback=self.parse_category)
            request.meta['item'] = item

            yield request

    def parse_category(self, response):
        articles = response.css("li.content-list__item.content-list__item_post.shortcuts_item")
        item = response.meta['item']

        i = 0
        for article in articles:
            article_link = article.css("article h2.post__title > a::attr(href)").extract_first()

            if i > 0:
                break

            request = scrapy.Request(url=article_link, callback=self.parse_each_article)
            request.meta['item'] = item

            i += 1
            yield request

    def parse_each_article(self, response):
        item = response.meta['item']

        article_date = response.css("article.post.post_full header.post__meta span::attr(data-time_published)").extract_first()
        article_name = response.css("article.post.post_full h1.post__title.post__title_full span::text").extract_first()
        article_content_block = response.css("div.post__body.post__body_full > div#post-content-body")
        article_content = article_content_block.extract_first()
        article_content = w3lib.html.remove_tags(article_content)
        article_parsed_date = datetime.now()
        article_author = response.css("a.post__user-info.user-info span::text").extract_first()

        article_images = response.css("div.post__body.post__body_full > div#post-content-body img::attr(src)")

        images = {}

        position = 0
        for image in article_images:
            images[position] = image.extract()
            position += 1

        item['name'] = article_name
        item['content'] = article_content
        item['author'] = article_author
        item['date'] = article_date
        item['parsed_date'] = article_parsed_date
        item['source'] = response.url
        item['images'] = images

        yield item
