from baike_spider1 import url_manager
from baike_spider1 import html_downloader
from baike_spider1 import html_parser
from baike_spider1 import html_outputer

class SpiderMain(object):#创建SpiderMain方法
    def __init__(self):
        self.urls = url_manager.UrlManager()#初始化启动管理器
        self.downloader = html_downloader.HtmlDownloader()#初始化启动下载器
        self.parser = html_parser.HtmlParser()#初始化启动解析器
        self.outputer = html_outputer.HtmlOutputer()#初始化启动输出器

    def craw(self, root_url):
        count = 1 #记录当前爬取的是第几个URL
        self.urls.add_new_url(root_url)#把入口URL添加进URL管理器
        while self.urls.has_new_url():#如果有待爬取的URL
            try:
                new_url = self.urls.get_new_url()#取第一个出来
                print('craw %d :%s' % (count, new_url))#打印出的URL是第几个URL
                html_cont = self.downloader.download(new_url)#下载对应页面
                new_urls,new_data  = self.parser.parse(new_url, html_cont)#下载好后，进行页面的解析，得到新的URL和数据
                self.urls.add_new_urls(new_urls)#把新的URL补充进URL管理器
                self.outputer.collect_data(new_data)#进行数据的收集

                if count ==10: #目标：爬取100个页面
                    break
                count = count + 1
            except Exception as e:
                print('craw failed!',e)
        self.outputer.output_html()#输出output收集下载好的数据

if __name__=="__main__":
    root_url="http://baike.baidu.com/view/21087.htm"#设置入口URL
    obj_spider = SpiderMain()#创建obj_spider
    obj_spider.craw(root_url)#调用SpiderMain的craw方法启动爬虫