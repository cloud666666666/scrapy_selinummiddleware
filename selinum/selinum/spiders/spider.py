import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
from selinum.items import SelinumItem

class SpiderSpider(scrapy.Spider):
    name = "spider"
    allowed_domains = ["spiderbuf.cn"]
    start_urls = ["http://spiderbuf.cn/playground/h05"]
    max_page = 1
    number = 1
    def parse(self, response):
        elements_list = response.xpath('//*[@id="dataContent"]/thead/tr[*]')
        for element in elements_list:
            item = SelinumItem()
            item['rank'] = self.number
            self.number += 1
            item['pwd'] = element.xpath('./td[2]/text()').get()
            item['timecost'] = element.xpath('./td[3]/text()').get()
            item['counts'] = element.xpath('./td[4]/text()').get()
            yield item

        # 检查是否需要加载下一页
        if self.max_page < 1:
            self.max_page += 1
            next_page_url = f"http://spiderbuf.cn/playground/n03/{self.max_page}"
            yield scrapy.Request(next_page_url, callback=self.parse)

