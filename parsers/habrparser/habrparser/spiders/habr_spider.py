import scrapy, w3lib
from ..items import HabrparserItem, ImageItem
from datetime import datetime
import time, re, os
from ..pipelines import ArticlesTable
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class HabrSpider(scrapy.Spider):
    name = "habr"
    main_url = 'https://habr.com/ru/'

    def start_requests(self):
        urls = [
            'https://habr.com/ru/',
        ]

        # parser_inner_path = os.path.dirname(os.path.dirname(__file__))
        # parser_path = os.path.abspath(os.path.join(parser_inner_path, os.pardir))
        # database_path = os.path.abspath(os.path.join(parser_path, os.pardir))
        # self.engine = create_engine("sqlite:///%s\sciheralddb.sqlite3"%("C:\DjangoSites\sciherald\\"), echo=False)
        # self.session = Session(bind=self.engine)
        
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

            category_link = category.css('a::attr(href)').extract_first()
            category_name = category.css('a::text').extract_first()

            item = HabrparserItem()
            item['category'] = category_name
            
            request = scrapy.Request(url=category_link, callback=self.parse_category)
            request.meta['item'] = item

            yield request

    def parse_category(self, response):
        item = response.meta['item']

        last_page_url = response.css("ul#nav-pagess > li")[-1]
        last_page_url = last_page_url.css("a::attr(href)").extract_first()
        # print("ЛАСТ:                   ", last_page_url)

        request = scrapy.Request(url="https://habr.com%s"%last_page_url, callback=self.go_to_last_page)
        request.meta['item'] = item

        yield request

    def go_to_last_page(self, response):
        item = response.meta['item']
        page_exists = response.css("ul.arrows-pagination > li")

        prev_page_url = page_exists[0].css("a#previous_page::attr(href)").extract_first()
        total_pages = response.css("span.toggle-menu__item-link.toggle-menu__item-link_pagination.toggle-menu__item-link_active::text").extract_first()

        for page in reversed(range(0, int(total_pages))):
            next_page_request = scrapy.Request(url="https://habr.com%s"%prev_page_url, callback=self.parse_each_page)
            next_page_request.meta['item'] = item

            yield next_page_request

            prev_page_url = re.sub(r'page\d+', 'page%s'%page, prev_page_url)

    def parse_each_page(self, response):
        item = response.meta['item']

        articles = response.css("li.content-list__item.content-list__item_post.shortcuts_item")

        """
            SELECT original_link FROM api_article WHERE source_id = 3 ORDER BY id
        """

        i = 0
        for article in articles:
            article_link = article.css("article h2.post__title > a::attr(href)").extract_first()

            if article_link == None:
                continue

            request = scrapy.Request(url=article_link, callback=self.parse_each_article)
            request.meta['item'] = item

            # if i > 0:
            #     break
            # i += 1
            yield request

    def parse_each_article(self, response):
        item = response.meta['item']

        article_date = response.css("article.post.post_full header.post__meta span::attr(data-time_published)").extract_first()
        article_name = response.css("article.post.post_full h1.post__title.post__title_full span::text").extract_first()
        article_content_block = response.css("div.post__body.post__body_full > div#post-content-body")
        article_content = article_content_block.extract_first()

        # article_content = w3lib.html.remove_tags(article_content)
        article_parsed_date = datetime.now()
        article_author = response.css("a.post__user-info.user-info span::text").extract_first()

        article_images = response.css("div.post__body.post__body_full > div#post-content-body img::attr(src)")

        images = {}
        images_list = []

        position = 0
        for image in article_images:
            image_url = image.extract()
            if image_url in article_content:
                article_content = article_content.replace('<img src="%s" alt="image">'%image_url, '~~%s~~'%position)
                images[position] = image_url
                position += 1
                images_list.append(image.extract())

        item['name'] = article_name
        item['content'] = article_content
        item['author'] = article_author
        item['date'] = article_date
        item['parsed_date'] = article_parsed_date
        item['source'] = 3
        item['original_link'] = response.url
        item['images'] = images
        item['image_urls'] = images_list

        yield item
