from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    def parse(self, new_url, html_con):
        if new_url is None or html_con is None:
            return
        soup = BeautifulSoup(html_con, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(new_url, soup)
        new_data = self.get_new_data(new_url, soup)
        return new_urls, new_data

    def get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/html/[A-Z\][0-9_]+.html"))  # /html/DQ301538.html
        for link in links:
            new_urlss = link['href']
            new_full_url = urllib.parse.urljoin(new_url, new_urlss)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, new_url, soup):
        res_data = {}
        res_data['url'] = new_url
        return res_data
