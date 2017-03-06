# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/22 17:33'


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print(message, 'from Parent')


class FooChild(FooParent):
    def __init__(self):
        # super调用FooParent的__init__
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    # 先通过子类的__init__调用父类的__init__,再子类的print
    # 再调用父类的bar，再子类的bar
    fooChild.bar('HelloWorld')

"""
Parent
Child
HelloWorld from Parent
Child bar fuction
I'm the parent.
"""