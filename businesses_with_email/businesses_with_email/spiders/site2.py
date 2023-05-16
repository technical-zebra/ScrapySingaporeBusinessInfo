import scrapy
from scrapy.http.request import Request
from ..items import BusinessesWithEmailItem


class site2(scrapy.Spider):
    name = 'site2'
    page_number = 2

    def start_requests(self):
        urls = ['https://www.siccmembers.com.sg/search/alphabetical'] #
        for x in range(2,34,1):
            urls.append('https://www.siccmembers.com.sg/search/alphabetical?ViewCompany_page='+str(x))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = BusinessesWithEmailItem()
        #15
        for x in range(1,16):
            try:
                business_name = response.css('div.lst-alpha:nth-child(' + str(x) + ') div.left-alpha h3 a::text').get()
                if business_name == None:
                    business_name2 = response.css(
                        'div.lst-alpha:nth-child(' + str(x) + ') div.left-alpha-full h3 a::text').get()
                    business_name = business_name2
                email = response.css('div.lst-alpha:nth-child(' + str(x) + ') p.email a::text').get()
                # print(business_name, business_name2, email)

                if email != None:
                    items['business_name'] = business_name
                    items['email'] = email
                    yield items
            except:
                pass

        # if business_name is None:
        #     yield Request(url=response.url, callback=self.parse, dont_filter=True)

        #
        # next_page = 'https://www.siccmembers.com.sg/search/alphabetical?ViewCompany_page='+ str(site2.page_number)
        # if site2.page_number < 34:
        #     site2.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)

