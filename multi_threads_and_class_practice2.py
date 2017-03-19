# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 multi_threads_and_class_practice2.py'
__author__ = 'zhiyi'
__date__ = '2017/3/19 10:33'
__vers__ = '1.0'
import requests
from bs4 import BeautifulSoup
import threading
import time
from multiprocessing import Queue
import os

class Mythread(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        # print(self.name, '  正在搞事情')
        self.res = self.func(*self.args)


class Mythread2(threading.Thread):
    def __init__(self, func, args, name):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        # print(self.name, '  正在解析')
        self.func(*self.args)

headers = {
    'Host': 'cd.58.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


def index_page():
    url = 'http://zhuanzhuan.58.com/?zzfrom=baidubradingPC3&zhuanzhuanSourceFrom=805'
    html = requests.get(url=url)
    soup = BeautifulSoup(html.text, 'lxml')
    get_links_tabs = soup.select('div.body_box2 > ul > li > a')
    links = []
    for get_links_tab in get_links_tabs:
        name = get_links_tab.text
        link = get_links_tab.get('href')
        # print(name, link)
        links.append(link)
    return links


def second_page(link, q):
    url = link
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    tabs = soup.select('#infolist > div:nth-of-type(2) > table > tbody > tr.zzinfo')
    for tab in tabs:
        title = tab.select('td.t > a')[0].text
        link = tab.select('td.t > a')[0].get('href')
        price = tab.select('td.t > span.pricebiao > span.price')[0].text
        print(title, link, price)
        value = [title, link, price]
        if not q.full():
            q.put(value)


def read_page(q):
    if not q.empty():
        value = q.get()
        # 设置了timeout就会一直爬下去..就算timeout了还会这样。为什么
        # 如果不设置timeout就是正常结束的
        try:
            html = requests.get(value[1], timeout=0.5)
            # html = requests.get(value[1])
            print(html.status_code, value[1])
        except:
            pass

if __name__ == '__main__':
    base_url = 'http://cd.58.com/diannao/pn{}/?zz=zz&PGTID=0d300023-0006-6c74-b645-53b121531468&ClickID=2'
    threads1 = []
    threads2 = []
    q = Queue()
    start_time = time.time()
    for i in range(1, 100):
        url = base_url.format(i)
        tc = Mythread(second_page, args=(url, q, ), name='我是第{}个虫子用来爬取'.format(i))
        # 放这基本读不到，太快了
        # tp = Mythread2(read_page, args=(q, ), name='我是第{}个虫子用来读取'.format(i))
        threads1.append(tc)
        tc.setDaemon(True)
        # threads2.append(tp)
        tc.start()
        # tp.start()

    for tc in threads1:
        tc.join()
        threads1.remove(tc)
        # print(tc.name + '已经结束爬取')

    MAX_THREADS = 100
    num = 1
    while True:
        if q.empty():
            break
        for t in threads2:
            if not t.is_alive():
                threads2.remove(t)
        if len(threads2) >= MAX_THREADS:
            time.sleep(0.25)
            print('我睡了0.2S')
            continue
        tp = Mythread2(read_page, args=(q, ), name='我是第{}个虫子用来解析'.format(num))
        threads2.append(tp)
        tp.setDaemon(True)
        tp.start()
        num += 1

    for tp in threads2:
        tp.join()
        print(tp.name + '已经结束解析')
        # 子进程没法结束啊、、这又是为啥
        threads2.remove(tp)

    end_time = time.time()
    total_time = end_time - start_time
    print('爬取完毕', total_time)
    import sys
    sys.exit(0)

