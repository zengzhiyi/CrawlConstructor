#only a test for which is written
from IPool import getIP
import requests
import random
import logs

url = 'http://www.baidu.com'
pro = getIP().getIPs()
for i in range(1000):
    try:
        proxies = random.choice(pro)
        html = requests.get(url, proxies=proxies, timeout=0.5)
        print(html, proxies, i)
    except Exception as e:
        logs.logHandler().getLog()
        pass
