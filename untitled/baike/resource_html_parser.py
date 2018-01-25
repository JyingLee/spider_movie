from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver


class ResourseHtml(object):

    def getResourse(self, datas):
        if datas is None:
            return
        for data in datas[1:]:
            # response = urllib.request.urlopen(data['url'])
            # if response.getcode() != 200:
            #     return

            driver = webdriver.PhantomJS()
            driver.get(data['url'])
            if driver.page_source is None:
                return
            soup = BeautifulSoup(driver.page_source, "html.parser")
            try:
                model = soup.find('div', class_='addss').find('input', type='text')
            except Exception as e:
                print("没有下载链接")
            if model is None:
                return
            print(model['value'])
