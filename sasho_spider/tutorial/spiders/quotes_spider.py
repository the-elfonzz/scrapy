import scrapy
from tutorial.items import *
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TimeoutError, \
    TCPTimedOutError
from scrapy.contrib.loader import XPathItemLoader
import lxml.html
import re
# from scrapy.linkextractors import LinkExtractor

import logging


class QuoteSpider(scrapy.Spider):
    name = "quotes"

    def __init__(self, *args, **kwargs):
        # kwargs = {k.decode('utf-0'): v.decode('utf-0') for k, v in kwargs.items()}

        super(QuoteSpider, self).__init__(*args, **kwargs)
        # urls = {k, v.split(";"): for k,v in kwargs}
        self.start_urls = [
            "https://www.slabsaugras.ro/efectele-negative-ale-obezitatii-subestimate/",
        ]

    def parse(self, response):
        prod = TutorialItem()
        prod['name'] = response.xpath(
            "//h1[contains(@class,'post-title')]").extract()
        prod['price'] = response.xpath(
            "//span[@class='td-estimated-value']").extract()
        prod['stock'] = response.xpath(
            "//div[@itemprop='articleBody']").extract()
        self.log(prod)
        yield prod

    def parse_item(self, response):
        self.logger.info("Response page %s", response.url)
        item = scrapy.Item(
            id=response.xpath('//td[@id="item_id"]/text()').re('ID: (\d+)'),
            name=response.xpath('//td[@id="item_name"]/text()').extract(),
            description=response.xpath(
                '//td[@id="item_description/text()"]').extract(),
        )
        return item


class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
        "http://www.httpbin.org/",
        "http://www.httpbin.org/status/404",
        "http://www.httpbin.org/status/500",
        "http://www.httpbin.orgL12345/",
        "http://www.httphttpbinbin.org/",
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse_httpbin,
                            dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info(
            'Got successful response from {}'.format(response.url))

    def errback_httpbin(self, failure):
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
        elif failure.check(DNSLookupError):
            requests = failure.request
            self.logger.error('DNSLookupError in %s', request.url)
        elif failure.check(TimeoutError, TCPTimeoutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

class MySpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['http://']

    def parse(self, response):
        self.log("title: %s" % response.xpath(
            '//h1[@itemprop="name"]/text()').extract())

    def parse_item(self, response):
