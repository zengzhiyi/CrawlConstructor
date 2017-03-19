# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 multi_process_queue.py'
__author__ = 'zhiyi'
__date__ = '2017/3/18 14:51'
__vers__ = '1.0'
from multiprocessing import Process, Queue, Pool
import os, time, random
import multiprocessing

# 写数据进程执行的代码:
def write(q, ):
# def write(q, lock):
    # lock.acquire()
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
    # lock.release()

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    print('所有数据都写入并且读完')

    # 创建进程池
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Pool()
    pw = p.apply_async(write, args=(q,))
    pr = p.apply_async(read, args=(q, ))
    p.close()
    p.join()

    # 加进程锁
    manager = multiprocessing.Manager()
    q = manager.Queue()
    lock = manager.Lock()
    p = Pool(4)
    # p.map_async(write, iterable=[])
    pw = p.apply_async(write, args=(q, lock))
    pr = p.apply_async(read, args=(q,))
    p.close()
    p.join()
