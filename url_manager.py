class UrlManager(object):
    def __init__(self):
        self.new_urls = set()#创建一个待爬取的URL列表
        self.old_urls = set()#创建一个爬取过的URL列表

    def add_new_url(self, url):#向管理器中添加单个URL
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:#既不在待爬取列表又不在已爬取列表
            self.new_urls.add(url)#用来爬取

    def add_new_urls(self, urls):#向管理器中添加多个URL
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)#调用add_new_url方法

    def has_new_url(self):#判断管理器中是否有新的待爬取的URL
        return len(self.new_urls) != 0

    def get_new_url(self):#从管理器中获取一个新的带爬取的URL
        new_url = self.new_urls.pop()#POP方法：从列表中获取这个URL并移除
        self.old_urls.add(new_url)
        return new_url

