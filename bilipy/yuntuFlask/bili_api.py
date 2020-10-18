# -*- coding: utf-8 -*-

import pprint
import json
from wordcloud import WordCloud
import jieba
from jieba import analyse
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random
import io
import re

def readfile(path):
    with io.open(path, 'rb') as f:
        data = f.read()
        f.close()
        return data

        # for root, dirs, files in os.walk('txts/'):
        #     for i in files:
        #         os.remove(root + i)

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)
background_Image = np.array(Image.open('1.jpg'))

wc = WordCloud(
    background_color='white',
    mask=background_Image,
    font_path=r'./SourceHanSerifCN-Medium.otf',

    color_func=random_color_func,
    random_state=50,
)

with open('stop_words.txt', 'rb') as f:
    stopWords = [line.decode('utf-8').replace('\r\n', '') for line in f.readlines()]

data = readfile('../txts/全站榜Content.txt')
wordList = jieba.cut(data)

# wordList =  [w for w in wordList if len(w)>1
#  and not re.match('^[a-z|A-Z|0-9|.]*$', w) ]

wordList = [w for w in wordList if w not in stopWords]
# print(wordList)
# print(wordList)
wordStr = " ".join(wordList)
# print(wordStr)
word_cloud = wc.generate(wordStr)
word_cloud.to_file('ss.jpg')
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
# tags = analyse.textrank(data, topK=30, withWeight=True)
# for i in tags:
#     print(i)