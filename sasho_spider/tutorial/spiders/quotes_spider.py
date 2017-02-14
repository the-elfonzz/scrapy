import scrapy
from tutorial.items import *
from scrapy.loader import ItemLoader
from tutorial.pipelines import *
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TimeoutError, TCPTimedOutError
from scrapy.linkextractors import LinkExtractor

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        # 'http://quotes.toscrape.com/',
       'http://pressonline.rs/rss-feeds.html'
    ]
    allowed_domains = ['http://www.example.com']

    # def start_requests(self):
    #     urls =
    #
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Save file %s' % filename)

    # def parse(self, response):
    #     self.logger.info('Response from %s arrived!', response.url)
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('span small::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract_first(),
    #         }
    #     next_page = response.xpath("//ul[@class='pager']//a/@href").extract_first()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

    # def parse(self, response):
    #     l = ItemLoader(item=Product(), response=response)
    #     l.add_xpath('name', '//div[@class="product_name"]')
    #     l.add_xpath('name', '//div[@class="product_title"]')
    #     l.add_xpath('price', '//p[@id="price"]')
    #     l.add_css('stocl', 'p#stock')
    #     l.add_value('last_updated', 'today')
    #     print l.load_item()
    #     return l.load_item()

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('name', '//div[@class="product_title"]')
        l.add_xpath('price', '//p[@id="price"]')
        l.add_css('stocl', 'p#stock')
        l.add_value('last_updated', 'today')
        print ("Existing settitngsL %s" % self.settings.attributes.key())
        print l.load_item()
        return l.load_item()

    def parse_item(self, response):
        self.logger.info("Response page %s", response.url)
        item = scrapy.Item(
            id=response.xpath('//td[@id="item_id"]/text()').re('ID: (\d+)'),
            name=response.xpath('//td[@id="item_name"]/text()').extract(),
            description=response.xpath('//td[@id="item_description/text()"]').extract(),
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
                                    #errback=self.errback_httpbin,
                                    dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))

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
