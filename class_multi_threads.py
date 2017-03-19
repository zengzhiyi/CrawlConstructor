# _*_ coding: utf-8 _*_
__file__ = '爬虫小框架 class_multi_threads.py'
__author__ = 'zhiyi'
__date__ = '2017/3/18 19:42'
__vers__ = '1.0'
import threading
from time import sleep, ctime

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):  # run()函数
        print("Starting", self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x - 2) + fib(x - 1))


# 阶乘函数 factorial calculation
def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x - 1))


# 求和函数
def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + sum(x - 1))


funcs = [fib, fac, sum]
n = 14


def main():
    nfuncs = range(len(funcs))

    print('*****单线程方法*****')
    for i in nfuncs:
        print('Starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print('Finished', funcs[i].__name__, 'at:', ctime())
    print('*****结束单线程*****')
    print('*****多线程方法*****')
    threads = []
    for i in nfuncs:
        # 调用MyThread类实例化的对象，创建所有线程
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

        # 开始线程
    for i in nfuncs:
        threads[i].start()

        # 等待所有结束线程
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('*****结束多线程*****')


if __name__ == '__main__':
    main()