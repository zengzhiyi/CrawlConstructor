#cannot figure out how to do it
import time
import datetime
import dbs

def clock(self):
    crawlTime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))

    # #deploy dbs to select crawlTime in sql
    # sql = '''SELECT * FROM %s'''
    # conn.execute(sql)
    # conn.commit()
    # dbsTime = datetime.datetime.strftime(sql)
    # delta = datetime.timedelta(days=5)
    #
    # if crawlTime - dbsTime >= 5:
    #     #deploy dbs to insert
