#create IP pools
import requests
from bs4 import BeautifulSoup
import random
import re

class getIP(object):
    def __init__(self):
        self.headers = {
            'Host':'www.66ip.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        }
        self.url = 'http://www.66ip.cn/nmtq.php?getnum=150&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip'

    def getIPs(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'lxml')
        ips = re.findall('(\d+.*?):(\d+)', soup.text)
        data = []
        for ip in ips:
            ic = ip[0]
            id = ip[1]
            rip = str(ic) + ':' + str(id)
            data.append(rip)
        print(len(data))
        return data

if __name__ == '__main__':
     IPS = getIP().getIPs()
     print(IPS)
