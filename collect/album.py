# -*- coding:utf-8 -*-
import json
import hashlib
import os
import re
import MySQLdb
from collect.custom.mysql import conn

db = conn.conn().getConn()

sql = "select * from tmp_shetu where wid != 0 group by title";
client = db.cursor(MySQLdb.cursors.DictCursor)
client.execute(sql)
data = client.fetchall()

for sub in data:
    title = sub['title']
    des = sub['des']
    sql = "select wid from tmp_shetu where title = '%s'" % (title);
    client = db.cursor(MySQLdb.cursors.DictCursor)
    client.execute(sql)
    widArr = client.fetchall()
    picNum = len(widArr)
    if picNum == 0:
        continue
    pids = []
    for pid in widArr:
        pids.append(int(pid['wid']))

    pidStr = ','.join(str(s) for s in pids)

    sql = "select id, substring(cdn_path, 1) as cdn, width, height from www_common_pics_01 where id in ("+pidStr+")"

    client = db.cursor(MySQLdb.cursors.DictCursor)
    client.execute(sql)
    picInfo = client.fetchall()
    picNum = len(picInfo)
    cover1 = ''
    cover2 = ''
    cover3 = ''
    if picNum == 0:
        continue
    if picNum >= 1:
        cover1 = picInfo[0]['cdn'] + '####qianku####'+str(picInfo[0]['width'])+'####'+str(picInfo[0]['height'])
    if picNum >= 2:
        cover2 = picInfo[1]['cdn'] + '####qianku####'+str(picInfo[1]['width'])+'####'+str(picInfo[1]['height'])
    if picNum >= 3:
        cover3 = picInfo[2]['cdn'] + '####qianku####'+str(picInfo[2]['width'])+'####'+str(picInfo[2]['height'])

    sql = "insert into www_common_albums_01(`name`,`desc`,cate_id, uid, weight_updated_time, cover1, cover2, cover3, pic_num, status, source) values ('%s', '%s', 26, 0, 0, '%s', '%s', '%s', %d, 0, 'qianku')" % (title, des, cover1, cover2, cover3, picNum)
    # print sql
    # os._exit(0);
    client = db.cursor()
    client.execute(sql)
    lastId = int(db.insert_id())
    db.commit()

    if lastId is not None:
        for pic in picInfo:
            sql = "insert into www_relate_pic_album (aid, pid) VALUE (%d, %d)" % (lastId, pic['id'])
            client = db.cursor()
            client.execute(sql)
            db.commit()

