# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/21 17:35'
from multiprocessing import Process, Pool, Queue
import time
import requests


def f(x):
    html = requests.get('http://www.baidu.com')
    print(html.status_code)

# 放在实际项目里，可能需要建一个大类塞进去
if __name__ == '__main__':
    p = Pool(10)
    # 建了10个进程，但是我要操作100次，所以十个一批
    n = 0
    times = time.time()
    li = range(10)

    # 法一
    # 一次性添加多个任务
    # p.map_async(f, iterable=li)

    # 法二
    # for i in li:
    #   li是可循环对象，i是每次的参数，这么就可以起到map+async的效果
    #     p.apply_async(f, args=(i,))
    #     n += 1
    #     print(n)

    pro_time1 = time.time() - times
    p.close()
    p.join()
    print(pro_time1)
