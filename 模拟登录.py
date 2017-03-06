# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/2/18 21:30'
import requests
from pytesser3 import Image
from io import BytesIO


headers = {
    'Host': 'jiaowu.swjtu.edu.cn',
    'Origin': 'http://jiaowu.swjtu.edu.cn',
    'Referer': "http://jiaowu.swjtu.edu.cn/service/login.jsp?user_type=student",
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}

# 得到验证码图片，并人工输入
def getCheckCode(session):
    """
    :param session:
    :return: 验证码
    """
    img_url = 'http://jiaowu.swjtu.edu.cn/servlet/GetRandomNumberToJPEG'
    headers = {
        'Host': 'dean.swjtu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': "http://dean.swjtu.edu.cn/search/index.jsp",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    img = session.get(img_url, headers=headers)
    imgs = Image.open(BytesIO(img.content))
    imgs.show()
    Checkcode = input('input your code：')
    return Checkcode, session


# 传递post请求
def login(Checkcode, session):
    """
    input函数会提示你输入教务的账号和密码
    :param Checkcode:
    :param session:
    :return:
    """
    user_id = input('please input your account')
    password = input('please input your secret')
    post_url = 'http://dean.swjtu.edu.cn/servlet/UserLoginSQLAction'
    headers = {
        'Host': 'dean.swjtu.edu.cn',
        'Origin': 'http://dean.swjtu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'Referer': "http://dean.swjtu.edu.cn/search/index.jsp",
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    data = {
        'OperatingSystem': "Windows",
        'Browser': "Chrome",
        'user_id': user_id,
        'password': password,
        'ranstring': Checkcode,
        'user_type': 'student',
    }
    session.post(post_url, headers=headers, data=data)
    return session


if __name__ == '__main__':
    session = requests.session()
    Checkcode, session = getCheckCode(session)
    session = login(Checkcode, session)
    html = session.get('http://dean.swjtu.edu.cn/search/index.jsp')
    # 查看返回的html源代码中有没有你的名字，如果有的话就代表模拟登录成功了。
    # 这样在以后的传递请求中，用session.get代替request.get即可，注意每次用get请求时都得用传入session到函数体内
    print(html.text)