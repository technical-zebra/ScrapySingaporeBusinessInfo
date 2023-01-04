import scrapy
from scrapy.http.request import Request
from ..items import BusinessesWithEmailItem


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e) - 1, 2):
        de += chr(int(e[i:i + 2], 16) ^ k)

    return de


class BusinessInfoSpider(scrapy.Spider):
    name = 'site3'

    def start_requests(self):
        urls = ['https://www.singapore-sme.com/beauty-wellness', 'https://www.singapore-sme.com/business-finance',
                'https://www.singapore-sme.com/restaurant-eateries', 'https://www.singapore-sme.com/fashion-and-accessories',
                'https://www.singapore-sme.com/healthcare_1', 'https://www.singapore-sme.com/financial-services',
                'https://www.singapore-sme.com/services', 'https://www.singapore-sme.com/it-electronics',
                'https://www.singapore-sme.com/home-appliances_1', 'https://www.singapore-sme.com/foreign-companies']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = BusinessesWithEmailItem()
        business_name = response.css("li[class='last-child'] span[itemprop = 'title']::text").get().replace(" & amp;", " & ")
        # body > form:nth-child(2) > div:nth-child(14) > div:nth-child(2) > div:nth-child(3) > #div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(7) > div:nth-child(4) > #div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > a:nth-child(1)

        email = response.css("div[id='description'] p:nth-child(1)").get()
        # #textemail
        if email.find('data-cfemail') != -1:
            email = email[email.index('data-cfemail="'):email.index('">[email protected]') + 1]
            email = email.replace('data-cfemail="', '').replace('">[email protected]', '')
            email = decodeEmail(email)
        else:
            email = ''

        if email != '':
            items['business_name'] = business_name
        items['email'] = email
        yield items

        if business_name is None:
            yield Request(url=response.url, dont_filter=True)
