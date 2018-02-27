# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class collectPipeline(object):
    def process_item(self, item, spider):
        return item

class ShetuPipeline(object):

    def __init__(self):
        self.times = 0;

    def process_item(self, item, spider):
        try:
            item['href'] = re.match(r'http://588ku.com/bj-zhuanti/(\S+)(/p[\d]+.html)|.html', item['href']).group(1)
        except:
            pass
        return item
