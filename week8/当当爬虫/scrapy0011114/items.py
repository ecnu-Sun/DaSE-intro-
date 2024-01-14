# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class movieItem(scrapy.Item):
    title = scrapy.Field()
    rank = scrapy.Field()
    theme = scrapy.Field()


class dangdangbook(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    author = scrapy.Field()
    discribe = scrapy.Field()
