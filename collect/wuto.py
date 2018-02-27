# -*- coding:utf-8 -*-
import json
import hashlib
import os
from collect.custom.mysql import conn
# os._exit(0)
f = open('quotes-qianku-base.json', 'r')

data = json.load(f)
handleData = {}
# i = 0
for sub in data:
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

    sql = "insert into tmp_shetu (title, type, keyword, des, pid, wid, link) values ('%s', '%s', '%s', '%s', %d, 0, '%s')" % (sub['subTitle'].encode('utf-8'), sub['subType'].encode('utf-8'), (','.join(sub['subKeyword'])).encode('utf-8'), sub['subDesc'].encode('utf-8').replace("千库", "爱集"), int(sub['subIds']), sub['href'])
    # print sql
    # os._exit(0)
    db = conn.conn().getConn()
    client = db.cursor()
    client.execute(sql)
    db.commit()
