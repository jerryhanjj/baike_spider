# !/usr/bin/env python3

import html_downloader
import html_outputer
import html_parser
import url_manager

class SpiderMain(object):
    # 使用html的URL管理器、下载器、解析器、输出器
    # 默认构造，创建对象时执行
    def __init__(self):
        self.urls = url_manager.UrlManager()                # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器
        self.parser = html_parser.HtmlParser()              # 解析器
        self.outputer = html_outputer.HtmlOutputer()        # 输出器

    # 爬虫调度程序
    def craw(self,root_url):
        # 爬取 url 计数
        count = 1
        # 将 root_URL添加到URL管理器中,之后启动爬虫的循环
        self.urls.add_new_url(root_url)
        # 启动循环
        while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                # 启动下载器 下载页面内容
                html_content = self.downloader.download(new_url)
                # 解析网页内容，得到新的 网页列表、数据
                new_urls, new_data = self.parser.parse(new_url, html_content) # 参数 （当前爬取url，页面数据）
                # 对 URL、数据 进行分别处理
                # 处理 url，将解析的URL添加到url管理器
                self.urls.add_new_urls(new_urls)                 # 添加了批量的 url 到 管理器中
                #处理 数据，将解析的数据存入输出器
                self.outputer.collect_data(new_data)
                # 输出 爬虫 信息
                print("crawle %d: %s\n" % (count, new_url))
                # 设置循环条件
                if count == 100:
                    break
                count = count + 1
        self.outputer.output_html()

if __name__ == "__main__":
    # root_url 入口链接
    root_url = "http://baike.baidu.com/view/125370.htm"
    # 创建一个爬虫
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
