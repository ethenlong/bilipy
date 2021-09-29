# -*- coding: utf-8 -*-
import scrapy
import io
import os
import time
from bilipy.items import BilipyItem
from bilibili_api import video
import bilibili_api
SESSDATA = '810758c5%2C1606366695%2C35df9*51'
CSRD = 'ab39f9fb709768893fc3767c80869736'
class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com/']
    base_url = 'https://www.bilibili.com/v/popular/rank/'
    rank_type = {
        'all': ['all', '全站榜'],
        'origin': ['origin', '原创榜'],
        'rookie': ['rookie', '新人榜'],
        'life': ['life', '生活榜'],
        'digital': ['digital', '数码榜'],
        'food': ['food', '美食榜'] 
    }



    # 爬虫开始的函数，向调度器发送url并指定回调函数
    def start_requests(self):

        # 调用类中的变量要加self
        for value in self.rank_type.values():
            url = self.base_url + value[0]
            # print(url)
            yield scrapy.Request(url, callback=self.parse)

    def openfile(self, path, content):
        with io.open(path, 'a+', newline='', encoding='gb18030') as f:
            f.write(content + " ")
            f.close()

    def parse(self, response):
        item = BilipyItem()
        # 获得请求的url地址
        url = response.url
        item['set_name'] = url.split('/')[6].split('?')[0]
        # print(item['set_name'])
        item['rank_type'] = self.rank_type[item['set_name']][1]
        # print(response.text)
        # 直接对response进行xpath解析，得到选择器对象的列表 //*[@id="app"]/div[2]/div[2]
        info_list = response.xpath("//div[@class='rank-list-wrap']/ul/li")
        # print(info_list)
        # 遍历每一个li元素
        for info in info_list:
            urls = info.xpath(".//div[@class='info']/a/@href")[0].extract()
            if 'bangumi' in urls:
                pass
            else:
                bvid = urls.split('/')[4]
                danmu = video.get_danmaku(bvid=bvid)
                for i in danmu:
                    self.openfile('txts/'+ item['rank_type'] + 'Content.txt', i.text)
                titleTxt = info.xpath(".//div[@class='info']/a/text()")[0].extract()
                self.openfile('txts/' + item['rank_type']+'Titles.txt', titleTxt)
                tags = video.get_tags(bvid=bvid)
                for tag in tags:
                    self.openfile('txts/'+ item['rank_type'] + 'Tags.txt', tag.text)
            time.sleep(0.1)





            item['rank_no'] = info.xpath("./div[@class='num']/text()")[0].extract()
            item['title'] = info.xpath(".//div[@class='info']/a/text()")[0].extract()
            # 这里是一个li元素里面，所以xpath解析出来只有3个元素,索引取值即可
            detals = info.xpath(".//span/text()")
            item['play_num'] = detals[0].extract()
            item['comment_num'] = detals[1].extract()
            item['uploader'] = detals[2].extract()
            item['score'] = info.xpath(".//div[2]/div/text()")[0].extract()
            yield item