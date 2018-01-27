from bs4 import BeautifulSoup
from selenium import webdriver
import mysql.connector
import threading


class ResourseHtml(object):

    def getResourse(self, datas):
        if datas is None:
            return
        print('共有资源长度:', len(datas))
        for data in datas:
            # response = urllib.request.urlopen(data['url'])
            # if response.getcode() != 200:
            #     return

            newThread = threading.Thread(target=self.spiderThread, args=(data,))
            newThread.start()
            newThread.join()

    def spiderThread(self, data):
        lock = threading.Lock()
        lock.acquire()
        try:
            driver = webdriver.PhantomJS()
            driver.get(data['url'])
            if driver.page_source is None:
                return
            soup = BeautifulSoup(driver.page_source, "html.parser")
            try:
                link = soup.find('div', class_='addss')
                if link is not None:
                    link = soup.find('div', class_='addss').find('input', type='text')
                else:
                    link = soup.find('div', class_='adds').find('input', type='checkbox')
                pic = soup.find('div', class_='pic').find('img')
                title = soup.find('h1')
            except Exception as e:
                print("该链接没有资源:" + data['url'])
                return
            if link is None or pic is None or title is None:
                return
            else:
                print(link['value'] + '\n' + pic['src'] + '\n' + title.get_text())
                conn = mysql.connector.connect(user='root', password='', database='spider_movie')
                cursor = conn.cursor()
                cursor.execute(
                    'create table if not exists movies(id INT(255) not null PRIMARY KEY AUTO_INCREMENT,'
                    'movie_name VARCHAR(255) NOT NULL UNIQUE,'
                    'pic VARCHAR(255) NOT NULL ,'
                    'link VARCHAR(255) NOT NULL )')
                cursor.execute('insert into movies(movie_name,pic,link) VALUES (%s,%s,%s)',
                               [title.get_text(), pic['src'], link['value']])
                conn.commit()
                cursor.close()
        finally:
            lock.release()
