# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/21 11:03'
# 最后决定的思路：
# 两个实体表 一个关系表
# 用yield迭代，有需要就插入数据库没有就拉倒

from bs4 import BeautifulSoup
import requests
import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       user='localhost',
                       password='123456',
                       db='test_zz',
                       charset='utf8')
cursor = conn.cursor()


def channel(cursor, conn):
    html = requests.get('http://zhuanzhuan.58.com/?zzfrom=baidubradingPC3&zhuanzhuanSourceFrom=805')
    soup = BeautifulSoup(html.text, 'lxml')
    cates = soup.find('div', {'class': 'body_box2'}).ul.find_all('a')
    for cate in cates:
        name = cate.text
        url = cate.attrs['href']
        sql = 'INSERT INTO test_zz.zz_channel(cate, url) VALUES ("{name}", "{url}")'.format(name=name, url=url)
        cursor.execute(sql)
        conn.commit()
        print('channel', name, url)
        yield (name, url)


def index(name, url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    rows = soup.find_all('tr', {'class': 'zzinfo'})
    sql = 'SELECT id FROM test_zz.zz_channel WHERE cate="{cate}"'.format(cate=name)
    cursor.execute(sql)
    cateID = cursor.fetchone()[0]
    print(cateID)
    for row in rows:
        title = row.find('td', {'class': 't'}).a.text
        url = row.find('td', {'class': 't'}).a.attrs['href']
        sql = 'INSERT INTO test_zz.zz_index(cateID, titile, url) VALUES ("{cateID}", "{title}", "{url}")'.format(cateID=cateID, title=title, url=url)
        cursor.execute(sql)
        conn.commit()
        print(cateID, title, url)
        short = title
        yield short, url


def detail(title, url):
    if url:
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'lxml')
        title = soup.find('div', {'class': 'col_sub mainTitle'}).find('h1').text
        time = soup.find('li', class_='count').text
        count = soup.find(id='totalcount').text
        price = soup.find('span', {'class': 'price c_f50'}).text
        sql = 'INSERT INTO test_zz.zz_detail(cateID, title, "time", "count", price) VALUES ()'
        print(title, time, count, price)

for name, url in channel(cursor, conn):
    for short, url in index(name=name, url=url):
        detail(short, url)


# 去重功能调用fetcher.py文件
# def add_new_url(url):
#     new_pages = set()
#     if url:
#         if url not in new_pages and url not in old_pages:
#             new_pages.add(url)


