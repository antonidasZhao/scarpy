# -*- coding:utf-8 -*-
import scrapy
import re
import os
from ..custom.mysql import conn
from ..items import  ShetuItem
import time

class ShetuSpider(scrapy.Spider):
    name = 'shetu'

    def __init__(self):
        self.parms = {
            'urls': []
        }

    def start_requests(self):
        urls = [
            'http://588ku.com/png-zhuanti/p1'
            'http://588ku.com/png-zhuanti/p2',
            'http://588ku.com/png-zhuanti/p3',
            'http://588ku.com/png-zhuanti/p4',
            'http://588ku.com/png-zhuanti/p5',
            'http://588ku.com/png-zhuanti/p6',
            'http://588ku.com/png-zhuanti/p7',
            'http://588ku.com/png-zhuanti/p8',
            'http://588ku.com/png-zhuanti/p9',
        ]
        self.parms['urls'] = urls;
        for url in urls:
           yield scrapy.Request(url, self.parse)

    def parse(self, response):
        if(response.url in self.parms['urls']):
            for quote in response.xpath('/html/body/div[4]/div[1]/div'):
                # item = ShetuItem()
                # name = quote.xpath('div/a/div[1]/h2/text()').extract_first()
                href = quote.xpath('div[1]/a/@href').extract_first()
                self.parms['action'] = 2
                self.parms['href'] = href
                # time.sleep(1)
                yield scrapy.Request(href, self.parse)

            for quote in response.xpath('/html/body/div[4]/div[2]/div'):
                # item = ShetuItem()
                # name = quote.xpath('div/a/div[1]/h2/text()').extract_first()
                href = quote.xpath('div[1]/a/@href').extract_first()
                self.parms['action'] = 2
                self.parms['href'] = href
                # time.sleep(1)
                yield scrapy.Request(href, self.parse)
            for quote in response.xpath('/html/body/div[4]/div[3]/div'):
                # item = ShetuItem()
                # name = quote.xpath('div/a/div[1]/h2/text()').extract_first()
                href = quote.xpath('div[1]/a/@href').extract_first()
                self.parms['action'] = 2
                self.parms['href'] = href
                # time.sleep(1)
                yield scrapy.Request(href, self.parse)
        else:
            for quote in response.xpath('//*[@id="png-pic-box"]/li'):
                item = ShetuItem()
                item['subIds'] = quote.xpath('div[1]/div/a[1]/@data').extract_first()
                item['action'] = self.parms['action']
                item['href'] = quote.xpath('div[1]/a/@href').extract_first()
                item['subTitle']=quote.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').extract_first()
                item['subType'] = quote.xpath('/html/body/div[3]/div/div/b/text()').extract_first()
                item['subDesc'] = quote.xpath('/html/body/div[3]/div/div/p/text()').extract_first()
                item['subKeyword'] = []
                for sub in quote.xpath('/html/body/div[3]/div/div/div[2]/div/div/a'):
                  item['subKeyword'].append(sub.xpath('text()').extract_first())
                yield item
            # for quote in response.xpath('//*[@id="across-floor"]/li'):
            #     item = ShetuItem()
            #     item['subIds'] = quote.xpath('div/a[1]/@data').extract_first()
            #     item['action'] = self.parms['action']
            #     item['href'] = response.url
            #     item['subTitle']=quote.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').extract_first()
            #     item['subType'] = quote.xpath('/html/body/div[3]/div/div/b/text()').extract_first()
            #     item['subDesc'] = quote.xpath('/html/body/div[3]/div/div/p/text()').extract_first()
            #     item['subKeyword'] = []
            #     for sub in quote.xpath('/html/body/div[3]/div/div/div[2]/div/div/a'):
            #         item['subKeyword'].append(sub.xpath('text()').extract_first())
            #
            #     yield item

            for quote in response.xpath('/html/body/div[4]/div/div/div/a'):
                href = quote.xpath('@href').extract_first()
                next_page = quote.xpath('text()').extract_first()
                try:
                    next_page = int(next_page)
                    if(next_page != 0 and next_page != 1 and href is not None):
                        yield scrapy.Request(href, self.parse)
                except:
                    pass






        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, self.parse)