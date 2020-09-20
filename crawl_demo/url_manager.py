class UrlManager:
    def __init__(self):
        self.old_urls = set()
        self.new_urls = set()

    # 向管理器添加url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器添加批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:   # 为什么还要考虑urls长度为0
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        # return self.new_urls is not None     # 这个可以嘛?
        return len(self.new_urls) != 0

    # 从url管理器获取一个新的待爬取的url
    def get_new_url(self):
        waiting_url = self.new_urls.pop()
        self.old_urls.add(waiting_url)
        return waiting_url
