# -*- coding:utf-8 -*-
import json
import hashlib
import os
import re
from collect.custom.mysql import conn
f = open('quotes-qianku-data.json', 'r')

data = json.load(f)
handleData = {}
db = conn.conn().getConn()
# i = 0
# def addslashes(s):
#     d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
#     return ''.join(d.get(c, c) for c in s)
for sub in data:
    # print sub['username']
    # os._exit(0)
    # title = hashlib.md5(sub['subTitle'].encode('utf-8')).hexdigest()
    #
    # if(handleData.has_key(title) != True):
    #     handleData[title] = {}
    #
    # if (handleData[title].has_key('id') != True):
    #     handleData[title]['id'] = []
    # handleData[title]['title'] =  sub['subTitle'];
    # handleData[title]['id'].append(sub['subIds']);
    # handleData[title]['type'] = sub['subType'];
    # handleData[title]['keyword'] = ','.join(sub['subKeyword']);
    # handleData[title]['des'] = sub['subDesc'];
    # i = i+1
    # if(i == 10):
    #     break;

# for subData in handleData:
#     db = conn.conn().getConn()
#     client = db.cursor()
#     sql = "select last_id from tmp_scrapy limit 1"
#     client.execute(sql)
#     db.commit()
    id = re.match(r'(.*?)(\d+).html', sub['href']).group(2)
    link = sub['href']
    if(sub['box'] is not None):
         rst = re.match(r'(\d+)\*(\d+)px', sub['box'])
    if(rst is None):
        width = 0
        height = 0
    else:
        width = int(rst.group(1))
        height = int(rst.group(2))
    imgArr = sub['img'].split('!')
    img = imgArr[0][21:]
    keyword = ','.join(sub['keyword'])
    if(sub['format'] is None):
        format = ''
    else:
        format = sub['format']
    # print link
    # print width
    # print height
    # print img
    # print format
    # sql = "select * from source_pic_qianku where source_id = %d" % (int(id))
    # client = db.cursor()
    # client.execute(sql)
    # exist = client.fetchall()
    # if len(exist) != 0:
    #     sql = "update source_pic_qianku set format = '%s' where source_id = %d" % (format, int(id))
    #     client = db.cursor()
    #     client.execute(sql)
    #     db.commit()
    # else:
    sql = "insert ignore into tmp_handle_data (title, tag, cdn_path, width, height, link, cid, source, uid, weight_updated_time) values ('%s', '%s', '%s', '%d', '%d', '%s', '%d', '%s', 0, 0)" % (sub['title'], keyword, img, width, height, link, 26, 'qianku')
    client = db.cursor()
    client.execute(sql)
    db.commit()

    # sql = "update tmp_shetu set link = '%s' where pid = %d" % (link, int(id))
    # client = db.cursor()
    # client.execute(sql)
    # db.commit()
        # lastId = 123
        # if(lastId is not None):
        #     sql = "insert into source_pic_qianku (id, source_id, username, width, height, format) values (%d, %d, '%s', '%s', %d, %d, '%s')" % (int(lastId), int(id), str(addslashes(sub['username'].encode('utf-8'))), int(width), int(height), format)
        #     print sql
        #     iexit
        #     client = db.cursor()
        #     client.execute(sql)
        #     db.commit()
    # os._exit(0)
    # sql = "insert into tmp_shetu (title, type, keyword, des, pid, link, wid) values ('%s', '%s', '%s', '%s', %d, '', 0)" % (sub['subTitle'].encode('utf-8'), sub['subType'].encode('utf-8'), (','.join(sub['subKeyword'])).encode('utf-8'), sub['subDesc'].encode('utf-8'), int(sub['subIds']))
    # # print sql
    # # os._exit(0)
    # db = conn.conn().getConn()
    # client = db.cursor()
    # client.execute(sql)
    # db.commit()
