# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 multi_threads.py'
__author__ = 'zhiyi'
__date__ = '2017/3/18 14:08'
__vers__ = '1.0'

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop: ', nloop, 'at: ', ctime())
    sleep(nsec)
    print('end loop: ', nloop, 'at: ', ctime())


def main():
    print('start at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print('all end:', ctime())

if __name__ == '__main__':
    main()
