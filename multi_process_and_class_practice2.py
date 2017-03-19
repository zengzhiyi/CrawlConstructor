# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/3/19 10:33'
__vers__ = '1.0'
import requests
from bs4 import BeautifulSoup
import threading
import time
from multiprocessing import Queue, Pool, Manager

headers = {
    'Host': 'cd.58.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}


def second_page(link, q, lock):
    # lock.acquire()
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
    # lock.release()


def read_page(q, lock):
    # lock.acquire()
    if not q.empty():
        value = q.get()
        html = requests.get(value[1], timeout=0.5)
        print(html.status_code, value[1])
    # lock.release()

if __name__ == '__main__':
    base_url = 'http://cd.58.com/diannao/pn{}/?zz=zz&PGTID=0d300023-0006-6c74-b645-53b121531468&ClickID=2'
    threads1 = []
    threads2 = []
    manager = Manager()
    lock = manager.Lock()
    q = manager.Queue()
    p = Pool(8)
    start_time = time.time()

    for i in range(100):
        url = base_url.format(i)
        p.apply_async(second_page, args=(url, q, lock, ))

    for i in range(3500):
        p.apply_async(read_page, args=(q, lock, ))

    p.close()
    p.join()

    # for i in range(4):
    #     p.apply_async(read_page, args=(q, lock, ))
    #
    # p.close()
    # p.join()

    end_time = time.time()
    total_time = end_time - start_time
    print('爬取完毕', total_time)

6882 - 3500
6889