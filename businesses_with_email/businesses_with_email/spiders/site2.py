import scrapy
from scrapy.http.request import Request
from ..items import BusinessesWithEmailItem

class site2(scrapy.Spider):
    name = 'site2'

    def start_requests(self):
        urls = ['https://www.siccmembers.com.sg/search/alphabetical']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = BusinessesWithEmailItem()
        business_name = response.css('div.left-alpha h3 a::text').getall()
        email = response.css('p.email a::text').getall()
        ##next_list = 'https://www.siccmembers.com.sg' + response.css('div.paging li.next a').xpath("@href").get()
        items['business_name'] = business_name
        items['email'] = email
        yield items

        # if next_list is not None:
        #     yield response.follow(next_list, callback=self.parse)
        #
        # if business_name is None:
        #     yield Request(url=response.url, dont_filter=True)
