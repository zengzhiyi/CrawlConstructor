#create connectiosn
#create tables
#insert into tables
#update into tables
import pymysql

class dataBases(object):
    def __init__(self):
        self.conn = pymysql.connect(host='', user='', password='', dbs='', charset='utf8')
        self.cursor = self.conn.cursor()

    def createTbs(self, **kwargs):
        sql = '''CREATE TABLE IF NOT EXISTS %s(

        UNIQUE (COLUMN_NAME )
        )'''

    def insertTbs(self, **kwargs):
        #当表设置了UNIQUE COLUMN后，可以使用
        #insert ignore into user_info (last_name,first_name) values ('','');
        #来忽略已存在数据库内的数据不再次插入数据库
        sql = '''INSERT INTO %s(


              )'''
        self.conn.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()
