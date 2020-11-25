# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class HabrparserPipeline:
#     def process_item(self, item, spider):
#         return item

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Session
import os
from habrparser.items import HabrparserItem
from scrapy.exceptions import DropItem

from scrapy.pipelines.images import ImagesPipeline

from . import settings

import scrapy
import time

Base = declarative_base()

class CategoriesTable(Base):
    __tablename__ = 'api_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %s>" % (self.name)


class SourcesTable(Base):
    __tablename__ = 'api_source'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category %s>" % (self.name)


class ArticlesTable(Base):
    __tablename__ = 'api_article'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("api_category.id"))
    content = Column(String)
    author = Column(String)
    date = Column(String)
    parsed_date = Column(String)
    source_id = Column(Integer, ForeignKey("api_source.id"))
    original_link = Column(String)

    def __init__(self, name, category_id, content, author, date, parsed_date, source_id, original_link):
        self.name = name
        self.category_id = category_id
        self.content = content
        self.author = author
        self.date = date
        self.parsed_date = parsed_date
        self.source_id = source_id
        self.original_link = original_link

    def __repr__(self):
        return "<Article %s, %s, %s, %s, %s, %s, %s>" % (self.name, self.category, self.content, self.author, self.date, self.parsed_date, self.source)


class ImagesTable(Base):
    __tablename__ = 'api_image'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("api_article.id"))
    path = Column(String)
    original_path = Column(String)
    position = Column(Integer)

    def __init__(self, article_id, path, original_path, position):
        self.article_id = article_id
        self.path = path
        self.original_path = original_path
        self.position = position

    def __repr__(self):
        return "<Image %s, %s, %s, %s>" % (self.article_id, self.path, self.original_path, self.position)


class HabrparserPipeline(object):
    def __init__(self):
        basename = 'data_scraped'
        parser_inner_path = os.path.dirname(os.path.dirname(__file__))
        parser_path = os.path.abspath(os.path.join(parser_inner_path, os.pardir))
        database_path = os.path.abspath(os.path.join(parser_path, os.pardir))
        # database_path = database_path.replace('\\', '\\\\')
        # self.engine = create_engine("postgresql://postgres:cao95records@localhost:5432/sciheralddb", echo=False)
        self.engine = create_engine("sqlite:///%s\sciheralddb.sqlite3"%("C:/Users/User/DjangoSites/sciherald"), echo=False)
        if not os.path.exists(basename):
            Base.metadata.create_all(self.engine)

    def get(self, model, **kwargs):
        """SqlAlchemy implementation of Django's get_or_create."""
        session = self.session
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return True
        else:
            return False

    def get_or_create(self, model, **kwargs):
        """SqlAlchemy implementation of Django's get_or_create."""
        session = self.session
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            instance = model(**kwargs)
            session.add(instance)
            session.flush()
            session.commit()
            return instance, True

    def process_item(self, item, spider):
        category, exists = self.get_or_create(CategoriesTable, name=item['category'])
        time.sleep(4)

        articles_table = ArticlesTable(
            item['name'],
            category.id,
            item['content'],
            item['author'],
            item['date'],
            item['parsed_date'],
            item['source'],
            item['original_link'],
        )

        article_exists = self.get(ArticlesTable, original_link=item['original_link'])

        if article_exists == False:
            self.session.add(articles_table)
            self.session.commit()

            # delete from api_image;
            # delete from api_article;
            # delete from api_category;

            if isinstance(item['images'], dict) and item['images'] != {}:
                changed_images = {}
                article_id = articles_table.id
                item['article_id'] = article_id
                for position, image_path in item['images'].items():
                    changed_images[article_id] = image_path
                    item['changed_images'] = changed_images
                    path = '/articles_images/%s/'%(article_id)
                    images_table = ImagesTable(
                        article_id,
                        path,
                        image_path,
                        position,
                    )

                    self.session.add(images_table)
                    self.session.commit()

        return item

    def close_spider(self, spider):
        # self.session.commit()
        self.session.close()

    def open_spider(self, spider):
        self.session = Session(bind=self.engine)


# class MyImagesPipeline(ImagesPipeline):

#     def file_path(self, request, response=None, info=None):
#         image_guid = response.meta['article_id']
#         print("AZAZA:                               ", '%s/%s' % (settings.IMAGES_STORE, image_guid))
#         return '%s/%s' % (settings.IMAGES_STORE, image_guid)

#     def get_media_requests(self, item, info):
#         for article_id, image_url in item['changed_images'].items():
#             # print("ARTICLE ID:        ", item['article_id'])
#             request = scrapy.Request(image_url)
#             # request.meta['article_id'] = article_id
#             # request.meta['article_id'] = item['article_id']

#             yield request

    # def item_completed(self, results, item, info):
    #     # image_paths = [x['path'] for ok, x in results if ok]
    #     # if not image_paths:
    #     #     raise DropItem("Item contains no images")
    #     # return item

    #     print("ITEM COMPLETED:                    ", [x for ok, x in results if ok])

    #     IMAGES_STORE = 'C:/DjangoSites/sciherald/staticfiles/images'

    #     if 'images_path' in item.fields:
    #         item['images_path'] = [x for ok, x in results if ok]

    #     return item

    # def item_completed(self, results, item, info):
    #     # iterate over the local file paths of all downloaded images
    #     import os
    #     for result in [x for ok, x in results if ok]:
    #         path = result['path']
    #         # here we create the session-path where the files should be in the end
    #         # you'll have to change this path creation depending on your needs
    #         target_path = os.path.join(("C:/DjangoSites/sciherald/staticfiles/images", os.basename(path)))
    #         print("TARGET:                      ", target_path)

    #         # try to move the file and raise exception if not possible
    #         if not os.rename(path, target_path):
    #             raise ImageException("Could not move image to target folder")
    #         # here we'll write out the result with the new path,
    #         # if there is a result field on the item (just like the original code does)
    #         # if self.IMAGES_RESULT_FIELD in item.fields:
    #             result['path'] = target_path
    #             item['images_path'].append(result)

    #     return item