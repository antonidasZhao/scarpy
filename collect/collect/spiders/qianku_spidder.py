# -*- coding:utf-8 -*-
import scrapy
import re
import os
from ..custom.mysql import conn
from ..items import  ShetuItem
import time

class QiankuSpider(scrapy.Spider):
    name = 'qianku'

    def __init__(self):
        self.parms = {
            'urls': [],
            'subUrls': []
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
        elif('http://588ku.com/png-zhuanti' in response.url):
            for quote in response.xpath('//*[@id="png-pic-box"]/li'):
                href = quote.xpath('div[1]/a/@href').extract_first()
                yield scrapy.Request(href, self.parse)
            for quote in response.xpath('/html/body/div[4]/div/div/div/a'):
                href = quote.xpath('@href').extract_first()
                next_page = quote.xpath('text()').extract_first()
                try:
                    next_page = int(next_page)
                    if(next_page != 0 and next_page != 1 and href is not None):
                        yield scrapy.Request(href, self.parse)
                except:
                    pass
        else:
            item = {}
            item['img']  = response.xpath('/html/body/div[2]/div[3]/div[1]/div/img/@src').extract_first()
            item['title'] = response.xpath('/html/body/div[2]/div[2]/span/text()').extract_first()
            item['keyword'] = []
            for quote in response.xpath('/html/body/div[2]/div[3]/div[3]/div[1]/a'):
                 item['keyword'].append(quote.xpath('text()').extract_first())
            item['box'] = response.xpath('/html/body/div[2]/div[3]/div[2]/div/ul/li[1]/b/text()').extract_first()
            item['format'] = response.xpath('/html/body/div[2]/div[3]/div[2]/div/ul/li[3]/b/text()').extract_first()
            item['href'] = response.url
            item['usernmae'] = response.xpath('/html/body/div[2]/div[3]/div[2]/div/div[3]/div[1]/a[2]/text()').extract_first()
            yield item










        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, self.parse)