# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 multi_threads_practice.py'
__author__ = 'zhiyi'
__date__ = '2017/3/18 15:44'
__vers__ = '1.0'
import requests
from bs4 import BeautifulSoup
import threading
from multiprocessing import Queue
import time

headers = {
    'Host': 'cd.58.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


def index():
    url = 'http://zhuanzhuan.58.com/?zzfrom=baidubradingPC3&zhuanzhuanSourceFrom=805'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    items = soup.find('div', {'class': 'body_box2'}).ul.find_all('li')
    links = []
    for item in items:
        name = item.find('a').get_text()
        link = item.find('a').attrs['href']
        print(name, link)
        links.append(link)
    return links


def second_index(link, q):
    html = requests.get(link, headers=headers)
    # print(html.status_code)
    soup = BeautifulSoup(html.text, 'lxml')
    tabs = soup.select('#infolist > div:nth-of-type(2) > table > tbody > tr')
    detail_links = []
    for tab in tabs:
        title = tab.select('td.t > a')[0].text
        price = tab.select('td.t > span.pricebiao > span')[0].text
        url = tab.select('td.t > a')[0].get('href')
        q.put(url)
        # detail_links.append(url)
        print(title, price, url)

    # return detail_links


def detail_page(links):
    for link in links:
        html = requests.get(link, headers=headers)
        print(html.status_code)


def run():
    threads = []
    base_url = 'http://bj.58.com/diannao/pn{}/?zz=zz&PGTID=0d300023-0000-17f1-e2ba-ee2c7dff35c7&ClickID=2'
    start_time = time.time()

    # 单线程
    # for i in range(2, 100):
    #     detail_links = second_index(base_url.format(i))
    #     print('这是第{}个虫子'.format(i-1))
    #     j = 0
    #     for link in detail_links:
    #         detail_page(link)
    #         print('详情页{}'.format(j))

    # 多线程,效率提升两倍左右
    q = Queue()
    for i in range(1, 100):
        t = threading.Thread(target=second_index, args=(base_url.format(i),), name='这是第{}个虫子'.format(i))
        threads.append(t)

    for i in threads:
        i.start()
    #
    # # 要实现多线程队列可能要创两个线程池才行
    # for j in range(1, 100):
    #     k = threading.Thread(target=detail_page, args=(, q, ))
    #     threads2.append(k)
    #     k.start()
    #
    # for j in threads2:
    #     j.join()

    for i in threads:
        i.join()

    end_time = time.time()
    all_time = end_time - start_time
    print('all is done', all_time)

if __name__ == '__main__':
    run()