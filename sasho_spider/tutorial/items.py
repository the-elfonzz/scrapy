from scrapy.item import Item, Field
# from scrapy_djangoitem import DjangoItem


class TutorialItem(Item):
	# define the fields for your item here like:
	name = Field()
	body = Field()
	last_updated = Field()
	pass


class Product(Item):
	name = Field()
	price = Field()
	stock = Field()
	last_updated = Field(serializer=str)


class PropertiesItem(Item):
	titile = Field()
	price = Field()
	description = Field()
	address = Field()
	image_urls = Field()
	images = Field()
	location = Field()
	url = Field()
	project = Field()
	spder = Field()
	date = Field()