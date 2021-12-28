import scrapy
from enum import Enum


class Currency(Enum):
    EUR = "EUR"
    HRK = "HRK"

class NjuskaloAd(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    published = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
