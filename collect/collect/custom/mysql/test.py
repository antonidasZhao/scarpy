import conn
mysqlConn = conn.conn()
client = mysqlConn.getConn()
sql = "select id from source_pic_wotu limit 10";
print client.execute(sql)
results = client.fetchall()
print results