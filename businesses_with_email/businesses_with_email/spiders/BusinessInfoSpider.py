import scrapy
import w3lib.html
from scrapy.http.request import Request
from ..items import BusinessesWithEmailItem


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e) - 1, 2):
        de += chr(int(e[i:i + 2], 16) ^ k)

    return de


class BusinessInfoSpider(scrapy.Spider):
    name = 'business_info'

    def start_requests(self):
        urls = ['https://www.singapore-sme.com/beauty-wellness', 'https://www.singapore-sme.com/business-finance',
                'https://www.singapore-sme.com/restaurant-eateries', 'https://www.singapore-sme.com/fashion-and-accessories',
                'https://www.singapore-sme.com/healthcare_1', 'https://www.singapore-sme.com/financial-services',
                'https://www.singapore-sme.com/services', 'https://www.singapore-sme.com/it-electronics',
                'https://www.singapore-sme.com/home-appliances_1', 'https://www.singapore-sme.com/foreign-companies']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        company_pages = response.css('div.listing-basicinfo a').xpath("@href").getall()
        next_list = response.xpath("//a[normalize-space()='>']/@href").get()
        company_pages = ["https://" + page if "https://" not in page else page for page in company_pages]
        for page_link in company_pages:
            yield Request(page_link, callback=self.parse_child_page, dont_filter=True)

        if next_list is not None:
            yield response.follow(next_list, callback=self.parse)

        if company_pages is None:
            yield Request(url=response.url, dont_filter=True)


    def parse_child_page(self, response):
        items = BusinessesWithEmailItem()
        business_name = response.css("li[class='last-child'] span[itemprop='title']::text").get().replace("&amp;", "&")
        email = response.css("div[id='description'] p:nth-child(1)").get()
        if email.find('data-cfemail') != -1:
            email = email[email.index('data-cfemail="'):email.index('">[email protected]') + 1]
            email = email.replace('data-cfemail="', '').replace('">[email protected]', '')
            email = decodeEmail(email)
        else:
            email = ''

        if email != '':
            items['business_name'] = business_name
            items['email'] = email
            yield items

        if business_name is None:
            yield Request(url=response.url, dont_filter=True)
