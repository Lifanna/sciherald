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
