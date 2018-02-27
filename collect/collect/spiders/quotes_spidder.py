# -*- coding:utf-8 -*-
import scrapy
import re
import os
from ..custom.mysql import conn

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    # os._exit(0)
    # start_urls = []
    #
    # db = conn.conn().getConn()
    # client = db.cursor()
    # sql = "select last_id from tmp_scrapy limit 1"
    # client.execute(sql)
    # lastIds = client.fetchall()
    # if len(lastIds) == 0:
    #     lastIds = [[0]]
    # if lastIds[0][0] >= 24699829:
    #     os._exit(0)
    # results = []
    # while 1:
    #     for lastId in lastIds:
    #         sql = "select id from source_pic_wotu where id > %d order by id asc  limit 1" % (int(lastId[0]));
    #         client.execute(sql)
    #         results = client.fetchall()
    #     if len(results) == 0:
    #         os._exit(0)
    #     picLastId = 0
    #     for picId in results:
    #         sql = "select id,link from www_common_pics_01 where id = " + str(picId[0]) + " limit 1"
    #         client.execute(sql)
    #         links = client.fetchall()
    #         if len(links) == 0:
    #             continue
    #         for link in links:
    #             sourceId = re.findall(r'\d+', link[1])
    #             sql = "insert ignore into www_common_picinfo (id, width, height, size, format, color_format, source_id, source, username) values (%d, 0, 0, 0, '', '', %d, 0, '')" % (picId[0], int(sourceId[0]))
    #             client.execute(sql)
    #             db.commit()
    #             start_urls.append(link[1])
    #     picLastId = picId[0]
    #     lastIds = [picId]
    #     if picLastId != 0:
    #         sql = "update tmp_scrapy set last_id = %d where id = 1" % (picLastId)
    #         print sql
    #         client.execute(sql)
    #         db.commit()
    #     if len(start_urls) != 0:
    #         break
    #
    #
    # def parse(self, response):
    #    data = {}
    #    i = 1
    #    #os.system("cd /www/tutorial && echo 1 > status")
    #    for quote in response.xpath('//div[@class="workInfor"]/p'):
    #      try:
    #          name = quote.xpath('//div[@class="workInfor"]/p['+str(i)+']/span[1]/text()').extract_first().strip().encode("utf-8")
    #          val = quote.xpath('//div[@class="workInfor"]/p['+str(i)+']/span[2]/text()').extract_first().strip().encode("utf-8")
    #          if name == "编号：" or name == "编号 ：":
    #              data['id'] = int(val)
    #          if name == "软件 ：" or name == "软件：":
    #              data['format'] = val
    #          if name == "颜色模式 ：" or name == "模式：" or name == "颜色模式：":
    #              data['color_format'] = val
    #          if(name == "印刷尺寸 ：" or name == "尺寸：" or name == "印刷尺寸："):
    #              box = re.findall(r'\d+', val)
    #              data['width'] = int(box[0])
    #              data['height'] = int(box[1])
    #          if(name == "体积 ：" or name == "体积："):
    #              size = re.findall(r'[\d\.]+', val)
    #              data['size'] = int(float(size[0])*1024*1024)
    #      except:
    #        pass
    #      i = i + 1
    #
    #    if data.has_key('format') or data.has_key('color_format'):
    #        pass
    #    else:
    #        data['color_format'] = response.xpath('//*[@id="pic"]/div[2]/div[2]/p[2]/span[2]/text()').extract_first()
    #        if data.has_key('width'):
    #            pass
    #        else:
    #            box = re.findall(r'\d+', response.xpath('//*[@id="pic"]/div[2]/div[2]/li/p[3]/span[2]/text()').extract_first().strip().encode("utf-8"))
    #            data['width'] = int(box[0])
    #            data['height'] = int(box[1])
    #            size = re.findall(r'[\d\.]+', response.xpath('//*[@id="pic"]/div[2]/div[2]/li/p[6]/span[2]/text()').extract_first().strip().encode("utf-8"))
    #            data['size'] = int(float(size[0]) * 1024 * 1024)
    #    if len(data) == 0:
    #        return
    #    if data.has_key('width'):
    #        pass
    #    else:
    #        data['width'] = 0
    #        data['height'] = 0
    #
    #    if data.has_key('color_format'):
    #        pass
    #    else:
    #        data['color_format'] = ''
    #
    #
    #    if data.has_key('format'):
    #        pass
    #    else:
    #        data['format'] = ''
    #    sql = "update www_common_picinfo set width = %d, height = %d, `size` = %d, format = '%s', color_format = '%s' where source_id = %d and source = 0" % (data['width'], data['height'], data['size'], data['format'], data['color_format'], data['id'])
    #
    #    sql = sql.replace('\\','\\\\')
    #    db = conn.conn().getConn()
    #    client = db.cursor()
    #    try:
    #      client.execute(sql)
    #      db.commit()
    #    except:
    #      db.rollback()
    #    db.close()

       # box = response.xpath('//*[@id="pic"]/div[2]/div[2]/p[6]/span[2]/text()').extract_first()
       # box = re.findall(r'\d+',box)
       # size = response.xpath('//*[@id="pic"]/div[2]/div[2]/p[8]/span[2]/text()').extract_first()
       # size = re.findall(r'\d+', size)
       # if box is None or size is None:
       #     return
       # else:
       #    width = box[0]
       #    height = box[1]
       # return {
       #  'format': response.xpath('//*[@id="pic"]/div[2]/div[2]/p[2]/span[2]/text()').extract_first(),
       #  'color_format':response.xpath('//*[@id="pic"]/div[2]/div[2]/p[3]/span[2]/text()').extract_first(),
       #  'width': width,
       #  'height': height,
       #  'size': size[0]
       # }