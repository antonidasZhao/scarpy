# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShetuItem(scrapy.Item):
    name = scrapy.Field()
    href = scrapy.Field()
    action = scrapy.Field()

    subKey = scrapy.Field()
    subType = scrapy.Field()
    subTitle = scrapy.Field()
    subKeyword = scrapy.Field()
    subDesc = scrapy.Field()
    subIds = scrapy.Field()
