# website_url_base = 'www.singapore-sme.com/'
# website_url_extensions = ['beauty-wellness', 'business-finance', 'restaurant-eateries', 'fashion-and-accessories',
#                          'healthcare_1', 'financial-services', 'services', 'it-electronics', 'home-appliances_1',
#                          'foreign-companies']
# start_url = [website_url_base + extension for extension in website_url_extensions]
# print(start_url)



# def parse(self, response):
#     title = response.css('title::text').get().split('-')
#     title = [t.strip() for t in title]
#     title = title[1]
#     description = response.css('div#description p')[0].extract()
#     description = description.strip().replace('\n', '').replace('\t', '').replace('</p>', '').replace('<p>',
#                                                                                                       '').split(
#         '<br>')
#     description = [x for x in description if x.find('Email') != -1]
#     # (x.find('Phone') != -1 or x.find('Email') != -1 or x.find('Website') != -1)
#     description = [decodeEmail(
#         x[x.index('data-cfemail='):x.index('>') + 1].replace('data-cfemail="', '').replace('">', '')) if (
#             x.find('Email') != -1) else x for x in description]
#     # description = w3lib.html.remove_tags(description)
#     yield {'titletext': title, 'description': description


# def decodeEmail(e):
#     de = ""
#     k = int(e[:2], 16)
#
#     for i in range(2, len(e)-1, 2):
#         de += chr(int(e[i:i+2], 16)^k)
#
#     return de

# print (decodeEmail('1a78757878636973775a787f7d68756f6a3479757734697d'))

# email = 'Email: <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="99eaf8f5fcead9f8ebf0f8f7b7faf6f4b7eafe">[email protected]</a><br>'
#
# a = email[email.index('data-cfemail='):email.index('>') + 1].replace('data-cfemail="', '').replace('">', '')
# print(a)
# print(decodeEmail(a))

