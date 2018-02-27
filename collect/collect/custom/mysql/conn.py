import MySQLdb
class conn:
    def __init__(self):
        self.dbConf = {
            'host' : '',
            'dbname': '',
            'username': '',
            'password': '',
            'charset': 'utf8'
        }
    def getConn(self):
        db = MySQLdb.connect(self.dbConf['host'], self.dbConf['username'], self.dbConf['password'], self.dbConf['dbname'])
        return db

