import scrapy


class MySpider(scrapy,):
    name = '163.com'
    allowed_domains = ['163.com']
    start_urls = [
        'http://www.163.comß'
    ]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)