# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class SelinumPipeline:
    def open_spider(self, spider):
        self.file = open('h05.csv', 'w', newline='',encoding='utf-8')
        self.fields_order = ['rank', 'pwd', 'timecost', 'counts']
        self.writer = csv.DictWriter(self.file, fieldnames=self.fields_order)
        self.writer.writeheader()
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
