# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 self_queue.py'
__author__ = 'zhiyi'
__date__ = '2017/3/18 21:18'
__vers__ = '1.0'
import threading
import time
import queue
# 到底用哪个？。。
from multiprocessing import Queue
import multiprocessing

class worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for tast" % (self.ident, self.name))
            try:
                task = q.get(block=True, timeout=20)  # 接收消息
            except queue.Empty:
                print("Nothing to do!i will go home!")
                self.thread_stop = True
                break
            print("task recv:%s ,task No:%d" % (task[0], task[1]))
            print("i am working")
            time.sleep(3)
            print("work finished!")
            q.task_done()  # 完成一个任务
            res = q.qsize()  # 判断消息队列大小
            if res > 0:
                print("fuck!There are still %d tasks to do" % (res))

    def stop(self):
        self.thread_stop = True


if __name__ == "__main__":
    q = queue.Queue(3)
    # q = multiprocessing.Queue(3)
    worker = worker(q)
    worker.start()
    q.put(["produce one cup!", 1], block=True, timeout=None)  # 产生任务消息
    q.put(["produce one desk!", 2], block=True, timeout=None)
    q.put(["produce one apple!", 3], block=True, timeout=None)
    q.put(["produce one banana!", 4], block=True, timeout=None)
    q.put(["produce one bag!", 5], block=True, timeout=None)
    print("***************leader:wait for finish!")
    q.join()  # 等待所有任务完成
    print("***************leader:all task finished!")