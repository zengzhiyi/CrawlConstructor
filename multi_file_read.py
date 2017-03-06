# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/26 12:07'
import os

# 读取dir下所有文件,\\是用来转义的
# root:每个文件夹下的“根”目录
# dirs:每个文件夹下的文件夹目录名
# file:每个文件夹下的文件名
# 如果不分开写则返回的目录都叠在一起，很乱
dir = 'G:\\pythonProjects\\djangoWeb\\mxonline5\\apps'
for root, dirs, files in os.walk(dir):
    for file in files:
        # endswith:知道意思吧
        if file.endswith(".py"):
            with open('codes.txt', 'a+', encoding='utf-8') as f:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as r:
                    rtext = r.read()
                    f.write(rtext)
                    print(rtext)

print('done')