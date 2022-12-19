import scrapy
import w3lib.html


def decodeEmail(e):
    de = ""
    k = int(e[:2], 16)

    for i in range(2, len(e) - 1, 2):
        de += chr(int(e[i:i + 2], 16) ^ k)

    return de


class BusinessInfoSpider(scrapy.Spider):
    name = 'business_info'
    # website_url_base = 'www.singapore-sme.com/'
    # website_url_extensions = ['beauty-wellness', 'business-finance', 'restaurant-eateries', 'fashion-and-accessories',
    #                          'healthcare_1', 'financial-services', 'services', 'it-electronics', 'home-appliances_1',
    #                          'foreign-companies']
    start_urls = ['https://www.singapore-sme.com/services/business-services/52']

    def parse(self, response):
        company_pages = response.css('div.listing-basicinfo a').xpath("@href").getall()
        next_list = response.css('a.searchPaginationNext').xpath("@href").getall()

        yield {'company_pages': company_pages, 'next_list': next_list}


        if len(next_list) < 1:
            next_page = next_list[0]
            yield response.follow(next_page, callback=self.parse())
