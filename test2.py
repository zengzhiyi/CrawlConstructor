# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/14 20:22'


def f():
    print(1 / 0)
for i in range(1000):
    try:
        f()
    except Exception:
        try:
            f()
        except Exception:
            print('shibailiangci')
            pass
