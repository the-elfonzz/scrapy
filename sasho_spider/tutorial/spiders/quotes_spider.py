import scrapy
from tutorial.items import *
from scrapy.loader import ItemLoadere
from tutorial.pipelines import *



class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        # 'http://quotes.toscrape.com/',
       'example.com'
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

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('name', '//div[@class="product_title"]')
        l.add_xpath('price', '//p[@id="price"]')
        l.add_css('stocl', 'p#stock')
        l.add_value('last_updated', 'today')
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
