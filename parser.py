#parse webpage
import requests
from bs4 import BeautifulSoup
import time
import datetime

class parser(object):
    def __init__(self):
        self.session = requests.session()

    def getHttp(self, urls, headers=None, proxies=None, timeout=5):
        html = self.session.get(urls, headers=headers, proxies=proxies, timeout=timeout).text
        return html

    def postHttp(self, urls, headers=None, data=None, proxies=None, timeout=5):
        html = self.session.post(urls, headers=headers, data=data, proxies=proxies, timeout=timeout)
        return html
