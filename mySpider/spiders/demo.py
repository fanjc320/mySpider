import scrapy


class DemoSpider(scrapy.Spider):
    name = "demo"
    # allowed_domains = ["app.mi.com"]
    # start_urls = ["https://app.mi.com"]
    # allowed_domains = ["app.mi.com"]
    # start_urls = ["https://www.qidian.com/rank/hotsales?style=1"]
    start_urls = ["https://www.quotes.toscrape.com/page/1/"]

    demo_settings = {
        # 'DOWNLOAD_DELAY': 270,  # 下载延迟 270秒
        # 'LOG_LEVEL': 'DEBUG',  # 打印日志等级
        # 下面两个设置 关闭SSL证书验证
        "DOWNLOAD_HANDLERS_BASE": {
            'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
            'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
            'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
            's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
        },
        "DOWNLOAD_HANDLERS": {
            'https': 'mySpider.demo.downloader.handler.https.HttpsDownloaderIgnoreCNError',
        },
    }
#//div[@class='quote']/span[@class='text']
#//div[@class='quote']//small[@class='author'] 或 //div[@class='quote']/span/small[@class='author']
#////div[@class='quote']/div[@class='tags']/a

    # def parse(self, response):
    #     print("crawler start working ... ".center(88, '-'))
    #     list_selector = response.xpath("//div[@class='book-mid-info'")
    #     list = []
    #     for one_selector in list_selector:
    #         name = one_selector.xpath("h4/a/text()").extract()[0]
    #         author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
    #         type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
    #         fr = one_selector.xpath("p[1]/span/text()").extract()[0]
    #         hot_dict = {
    #             "姓名": name,
    #             "作者": author,
    #             "类型": type,
    #             "获取方式": fr
    #         }
    #         print(hot_dict)
    #         list.append(hot_dict)
    #     return list


    def parse(self, response):
        print("crawler start working ... ".center(88, '-'))
        list_selector = response.xpath("//div[@class='quote']")
        list = []
        for one_selector in list_selector:
            text = one_selector.xpath("./span[@class='text']/text()").get()
            author = one_selector.xpath("./span/small/[@class='author']/text()").get()
            tags = one_selector.xpath("./div[@class='tags']/a/text()").getall()
            yield {"text":text, "author":author, "tags":tags}
        # next_url = response.xpath("//li[@class='next']/a/@href").get()
        # print("next_url:"+next_url)
        # if next_url is not None:
        #     yield scrapy.Request("http://quotes.toscrape.com"+next_url)










# 执行 scrapy crawl demo -o quotes1.json
# AttributeError: 'AsyncioSelectorReactor' object has no attribute '_handleSignals'
# 安装兼容的 Twisted 版本
# https://www.bytezonex.com/archives/htjVyKrE.html