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

Base = declarative_base()

class CategoriesTable(Base):
    __tablename__ = 'api_category'
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
        self.engine = create_engine("sqlite:///%s\sciheralddb.sqlite3"%("C:\DjangoSites\sciherald\\"), echo=False)
        if not os.path.exists(basename):
            Base.metadata.create_all(self.engine)

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

        self.session.add(articles_table)
        self.session.commit()

        # delete from api_image;
        # delete from api_article;
        # delete from api_category;

        if isinstance(item['images'], dict) and item['images'] != {}:
            for position, image_path in item['images'].items():
                article_id = articles_table.id
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
