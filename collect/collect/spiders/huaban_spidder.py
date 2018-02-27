# -*- coding:utf-8 -*-
import scrapy
import re
import os
from ..custom.mysql import conn
from ..items import  ShetuItem
import time
from scrapy_splash import SplashRequest

class QiankuSpider(scrapy.Spider):
    name = 'huaban'

    def __init__(self):
        self.parms = {
            'urls': [],
            'subUrls': []
        }

    def start_requests(self):
        urls = [
            'http://huaban.com/kkart/'
            # 'http://127.0.0.1'
        ]
        self.parms['urls'] = urls;
        for url in urls:
           yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print response.body
        os._exit(0)
        boardId = None
        if response.url in self.parms['urls']:
          for quote in response.xpath('//*[@id="water-fall"]/div'):
               try:
                   href = 'http://huaban.com' + quote.xpath('a[1]/@href').extract_first()
                   print href
                   os._exit(0)
                   boardId = quote.xpath('@data-id').extract_first()
                   nextPage = "http://huaban.com/jing-barbie/?jde3crhk&max="+boardId+"&limit=10&wfl=1"
                   yield scrapy.Request(href, self.parse)
               except:
                   pass
          for quote in response.xpath('//*[@id="waterfall"]/div'):
               try:
                   href = 'http://huaban.com' + quote.xpath('a[1]/@href').extract_first()
                   print href
                   os._exit(0)
                   boardId = quote.xpath('@data-id').extract_first()
                   nextPage = "http://huaban.com/jing-barbie/?jde3crhk&max="+boardId+"&limit=10&wfl=1"
                   yield scrapy.Request(href, self.parse)
               except:
                   pass

          if boardId is not None:
               yield scrapy.Request(nextPage, self.parse)
        elif 'http://huaban.com/boards' in response.url:
            url = response.url
            uname = response.xpath('//*[@id="board_card"]/div[2]/a/span/text()').extract_first()
            cateName = response.xpath('//*[@id="board_card"]/div[1]/div[1]/div/a/text()').extract_first()
            albumName = response.xpath('//*[@id="board_card"]/div[1]/div[1]/h1/text()').extract_first()

            for quote in response.xpath('//*[@id="waterfall"]/div'):
                pid = quote.xpath('@data-id').extract_first()
                link = quote.xpath('a/@href').extract_first()
                img = quote.xpath('a/img/@src').extract_first()
                imgTitle = quote.xpath('p[1]/text()').extract_first()
                yield {
                    'url': url,
                    'uname': uname,
                    'cateName': cateName,
                    'albumName': albumName,
                    'pid': pid,
                    'link': link,
                    'img': img,
                    'imgTitle': imgTitle
                }





