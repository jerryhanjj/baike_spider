import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# html 解析器 的实现
class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        if summary_node is None:
            res_data['summary'] = "None Summary!"
        else:
            res_data['summary'] = summary_node.get_text()

        return res_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 网页链接格式 /view/***.htm  ***代表多位数字
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))  # 正则表达式 \d+\ 表示数字
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls



