import urllib.request
import urllib.parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
import re
from selenium import webdriver

url = "http://www.yingshidaquan.cc/html/DQ295084.html"
# response = urllib.request.urlopen(url)
# data = response.read()
# print(data)
# data = data.decode('UTF-8')
# soup = BeautifulSoup(data, 'html.parser',from_encoding='utf-8')

# 获取所有a标签
# nodes = soup.find_all('a')
# for node in nodes:
#     print(node.name,node['href'],node.get_text())

# 获取其中的一个a标签http://news.baidu.com
# link=soup.find('a',href='http://news.baidu.com')
# print(link.name,link['href'],link.get_text())

# 通过正则表达式获取
# link=soup.find('a',href=re.compile(r"more"))
# print(link.name,link['href'],link.get_text())

# 获取指定标签内容
# link=soup.find('ul',class_='downurl')
# print(link)

# params={}
# params['word']='shabi'
# url_values=urllib.parse.urlencode(params)
# url="http://www.baidu.com/s?"
# full_url=url+url_values
# data1=urllib.request.urlopen(full_url).read()
# data1=data1.decode('UTF-8')
# print(data1)

# request=urllib.request.Request(url)
# request.add_header('user-agent','Mozilla/5.0')
# response1=urllib.request.urlopen(url)
# print(response1.getcode())

# cj=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cj)
# opener=urllib.request.build_opener(handler)
# r=opener.open(url)
# print(r.read())
# print(cj)

# 使用selenium
driver = webdriver.PhantomJS()
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
aa = soup.find('div', class_='addss')
if aa is not None:
    aa = soup.find('div', class_='addss').find('input', type='text')
if aa is None:
    aa = soup.find('div', class_='adds').find('input', type='checkbox')
print(aa)
print(aa['value'])
