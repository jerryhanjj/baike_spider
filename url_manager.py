# url 管理器的类
class UrlManager(object):
    # 两个存放不同URL的集合
    def __init__(self):
        # 初始化 待爬取 url 列表
        self.new_urls = set()
        # 初始化 已爬取 url 列表
        self.old_urls = set()

    # 添加单个URL到管理器
    def add_new_url(self, url):
        if url is None:
            return
        # 如果这个 URL 不在 待爬取 或者 已爬取 列表，则是一个 全新 的URL，添加到待爬取列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加URL到管理器
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)

    # 判断是否还有 未爬取的 url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一条新的未爬取的 url
    def get_new_url(self):
        # 获取一个URL并将此URL移除出new_urls列表
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url