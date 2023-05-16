# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd
import os

from itemadapter import ItemAdapter


class BusinessesWithEmailPipeline(object):
    def __init__(self):
        self.df = pd.DataFrame()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        business_name = adapter.get("business_name")
        email = adapter.get("email")
        # if email not in self.df['email'].values:
        #     df2 = pd.DataFrame({"business_name": [business_name],
        #                         "email": [email]})
        #     self.df = pd.concat([self.df, df2])

        df2 = pd.DataFrame({"business_name": [business_name],
                            "email": [email]})
        self.df = pd.concat([self.df, df2])
        return item

    def open_spider(self, spider):
        if os.path.exists("./data.csv"):
            os.remove("./data.csv")
        self.df['business_name'] = []
        self.df['email'] = []

    def close_spider(self, spider):
        self.df.to_csv("./data.csv", index=False)
