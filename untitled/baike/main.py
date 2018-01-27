from baike import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):  # 实例化对象
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # html下载器
        self.parser = html_parser.HtmlParser()  # html解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出

    def craw(self, root_url):
        count = 1  # 记录爬取数据的数量
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()  # 从url管理器获取一个新的url
                print("当前量:%d, 当前url:%s" % (count, new_url))
                html_con = self.downloader.download(new_url)  # 下载url页面
                new_urls, new_data = self.parser.parse(new_url, html_con)  # 解析url网页
                self.urls.add_new_urls(new_urls)  # 添加新解析到的批量的url
                self.outputer.collect_data(new_data)  # 收集需要的数据
                if count == 5:
                    break
                count += 1
            except Exception as e:
                print("url异常:", e)
        self.outputer.output_html()  # 输出数据


if __name__ == '__main__':
    root_url = "http://www.yingshidaquan.cc/html/dianying.html"  # 入口
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
