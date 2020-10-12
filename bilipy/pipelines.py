# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .settings import *

import csv
import io
class BilipyPipeline(object):
    def process_item(self, item, spider):
        return item

class CSVPipeline(object):
    # 可以实现写入一个csv文件的不同sheet吗？>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def process_item(self, item, spider):
        # 写入csv文件，需要设置encoding属性为gb18030(utf-8会出现乱码)
        with io.open(item['rank_type'] + '.csv', 'a+', newline='', encoding='gb18030') as f:
            writer = csv.writer(f)
            writer.writerow(
                [item['rank_no'], item['title'],
                 item['play_num'], item['comment_num'],
                 item['uploader'], item['score']
                 ])
        return item
