# -*- coding: utf-8 -*-
import scrapy

from conf import MAX_PAGE_COUNT
from ..items import Currency, NjuskaloAd
import re

def create_next_page_link(current_link, next_page_num):
    separator = '&' if '?' in current_link else '?'
    page = "{}{}page={}".format(current_link, separator, next_page_num)
    return page
    
class NjuskaloSpider(scrapy.Spider):
    name = 'njuskalo_spider'
    allowed_domains = ['njuskalo.hr']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = 'https://www.njuskalo.hr'

    def parse(self, response):
        try:
            articles = response.xpath("//ul[@class='EntityList-items' and count(.//div[@class='entity-pub-date']) > 0]/li/article")
            for article in articles:
                title = article.xpath(".//h3[@class='entity-title']/a/text()").extract_first().strip()
                link = self.base_url + article.xpath(".//h3[@class='entity-title']/a/@href").extract_first().strip()
                description = article.xpath(".//div[@class='entity-description-main']/text()").extract()
                description = ', '.join(filter(None, map(lambda s: s.strip(), description)))
                published = article.xpath(".//div[@class='entity-pub-date']/time/text()").extract_first().strip()
                
                try:
                    price = article.xpath(".//strong[@class='price price--eur']/text()").extract_first().strip().replace('.', '').replace(',', '')
                    currency = "EUR"
                except:
                    price = article.xpath(".//strong[@class='price price--hrk']/text()").extract_first().strip().replace('.', '').replace(',', '')
                    currency = "HRK"

                yield NjuskaloAd(
                    title=title,
                    link=link,
                    description=description,
                    published=published,
                    price=price,
                    currency=currency
                )

            try:
                next_page_num = response.css(".Pagination-item--next").xpath(".//button/@data-page").extract_first()
                if(not next_page_num):
                    raise "Next page BUTTON not found... Search for A HREF"
            except: 
                link = response.css(".Pagination-item--next").xpath(".//a/@href").extract_first()
                next_page_num = re.findall(r'\d+', link)[-1]

            if next_page_num and int(next_page_num) <= MAX_PAGE_COUNT:
                yield scrapy.Request(url=create_next_page_link(response.url, int(next_page_num)))
            else:
                print("Next page not found")

        except BaseException as e:
            print("Failed to scrape: ", e)


