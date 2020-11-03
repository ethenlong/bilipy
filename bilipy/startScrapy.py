from scrapy import cmdline
import os

def deltxt():
    for root, dirs, files in os.walk('txts/'):
        for i in files:
            os.remove(root + i)
            print(root + i)
deltxt()
cmdline.execute('scrapy crawl bilibili'.split())