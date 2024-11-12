import scrapy
from mySpider.items import MyspiderItem

class DemoSpider(scrapy.Spider):
    name = "demo"
    # allowed_domains = ["app.mi.com"]
    # start_urls = ["https://app.mi.com"]
    # allowed_domains = ["app.mi.com"]
    # start_urls = ["https://www.qidian.com/rank/hotsales?style=1"]
    # start_urls = ["https://www.quotes.toscrape.com/page/1/"]
    start_urls = ["https://quotes.toscrape.com"] # 去掉www就不会报Remote certificate is not valid for hostname
    # start_urls = ["https://quotes.toscrape.com/page/1"] # 去掉www就不会报Remote certificate is not valid for hostname

#//div[@class='quote']/span[@class='text']
#//div[@class='quote']//small[@class='author'] 或 //div[@class='quote']/span/small[@class='author']
#////div[@class='quote']/div[@class='tags']/a

    def parse(self, response):
        print("crawler start working ... ".center(88, '-'))
        list_selector = response.xpath("//div[@class='quote']")
        list = []
        for one_selector in list_selector:
            item = MyspiderItem()
            item['text'] = one_selector.xpath("./span[@class='text']/text()").get()
            item['author'] = one_selector.xpath("./span/small[@class='author']/text()").get()
            item['tags'] = one_selector.xpath("./div[@class='tags']/a/text()").getall()
            yield item
        next_url = response.xpath("//li[@class='next']/a/@href").get()
        # print("next_url:"+next_url) # 当next_url为空报错?
        if next_url is not None:
            print("next_url:" + next_url)
            yield scrapy.Request("http://quotes.toscrape.com"+next_url, callback = self.parse)










# 目录下执行 scrapy crawl demo -o quotes1.json
# AttributeError: 'AsyncioSelectorReactor' object has no attribute '_handleSignals'
# 安装兼容的 Twisted 版本
# https://www.bytezonex.com/archives/htjVyKrE.html
# scrapy 爬虫2小时入门（二）
# https://www.bilibili.com/read/cv10015858/