# _*_ coding: utf-8 _*_
__author__ = 'zhiyi'
__date__ = '2017/3/6 19:43'
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

constants = {}

constants['MAX_PAGE_TRIED'] = 5
number_tried = 0

while number_tried < constants['MAX_PAGE_TRIED']:
    try:
        driver = webdriver.PhantomJS()
        # 设置大一点的size，直接一次性加载完，否则又要用execute_script()进行操作
        driver.set_window_size(2500, 2500)
        url = 'http://product.dangdang.com/23760742.html'
        driver.get(url)

        # implicit waits
        # driver.implicitly_wait(10)

        # explicit waits
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "catalog-textarea"))
        )

        content = driver.page_source
        soup = BeautifulSoup(content, 'lxml')
        cates = soup.find(id='catalog-textarea')
        # if cates:
        cates = cates.get_text().replace('<br />', '')
        print(cates)
        number_tried += 1
        # break
    except IndexError:
        number_tried += 100
        print(IndexError)
    finally:
        driver.close()
        print('已经执行{s}次'.format(s=number_tried))
