# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilipyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 类型只有Field吗？>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    rank_type = scrapy.Field()         # 榜单类型
    rank_no = scrapy.Field()           # 排名
    title = scrapy.Field()             # 标题
    play_num = scrapy.Field()          # 播放数
    comment_num = scrapy.Field()       # 评论数
    uploader = scrapy.Field()          # 上传者
    score = scrapy.Field()             # 评分
    set_name = scrapy.Field()          # mongo中的库名
    pass
