# -*- coding: utf-8 -*-
import scrapy

from bilipy.items import BilipyItem
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com/']
    base_url = 'https://www.bilibili.com/ranking/'
    rank_type = {
        'all': ['all/0/0/3', '全站榜'],
        'origin': ['origin/0/0/3', '原创榜'],
        'bangumi': ['bangumi/13/0/3', '新番榜'],
        'cinema': ['cinema/177/0/3', '影视榜'],
        'rookie': ['rookie/0/0/3', '新人榜']
    }

    # 爬虫开始的函数，向调度器发送url并指定回调函数
    def start_requests(self):
        # 调用类中的变量要加self
        for value in self.rank_type.values():
            url = self.base_url + value[0]
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = BilipyItem()
        # 获得请求的url地址
        url = response.url
        item['set_name'] = url.split('/')[4]
        item['rank_type'] = self.rank_type[item['set_name']][1]
        # 直接对response进行xpath解析，得到选择器对象的列表
        info_list = response.xpath("//div[@class='rank-list-wrap']/ul/li")
        # 遍历每一个li元素
        for info in info_list:
            item['rank_no'] = info.xpath("./div[@class='num']/text()")[0].extract()
            item['title'] = info.xpath(".//div[@class='info']/a/text()")[0].extract()
            # 这里是一个li元素里面，所以xpath解析出来只有3个元素,索引取值即可
            detals = info.xpath(".//span/text()")
            item['play_num'] = detals[0].extract()
            item['comment_num'] = detals[1].extract()
            item['uploader'] = detals[2].extract()
            item['score'] = info.xpath(".//div[2]/div/text()")[0].extract()
            yield item