# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class HabrparserItem(Item):
    name = Field()
    category = Field()
    content = Field()
    author = Field()
    date = Field()
    parsed_date = Field()
    source = Field()
    original_link = Field()
    article = Field()
    images = Field()
    changed_images = Field()
    image_urls = Field()
    images_path = Field()
    article_id = Field()

class ImageItem(Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()


class ResJournalparserItem(Item):
    name = Field()
    category = Field()
    content = Field()
    author = Field()
    date = Field()
    parsed_date = Field()
    source = Field()
    original_link = Field()
    article = Field()
<<<<<<< HEAD
    images = Field()
=======
    images = Field()
>>>>>>> 86d1c7eee857fb0babd0008ef98353c136c0bf0e
