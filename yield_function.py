# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/22 21:10'

def yield_test(n):
    for i in range(n):
        c = (yield call(i))
        print(c, 'sha')
    print('done')

def call(i):
    return i*2

for i in yield_test(5):
    print(i, ',')