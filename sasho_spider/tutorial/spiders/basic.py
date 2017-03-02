# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ['http://']

    def parse(self, response):
        self.log("title: %s" % response.xpath(
        	'//*[@itemprop="name"][1]/text()').extract())
        self.log("price: %s" % response.xpath(
        	'//*[@itemprop="price"][1]/text()').re('[.0-9]+'))
        self.log("desctiption: %s" % response.xpath(
     		'//*[@itemprop="description"][1]/text()').extract())
        self.log("address: %s" % response.xpath(
        	'//*[@itemprop="http://schema.org/'
        	'Place"][1]/text()').extract())
        self.log("image_urls: %s" % response.xpath(
        	'//*[@otemprop="image"][1]/@src').extract())


