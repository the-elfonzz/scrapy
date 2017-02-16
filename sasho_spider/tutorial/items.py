import scrapy
# from scrapy_djangoitem import DjangoItem


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    body = scrapy.Field()
    last_updated = scrapy.Field()
    pass

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
