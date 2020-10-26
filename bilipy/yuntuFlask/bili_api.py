# -*- coding: utf-8 -*-

import pprint
import json
from wordcloud import WordCloud
import jieba
from jieba import analyse
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import io
import os

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


def addTitle(filepath, text, filename):
    setFont = ImageFont.truetype('./SourceHanSerifCN-Medium.otf', 40)
    fillColor = "#0000ff"
    size = (40, 40)
    image = Image.open(filepath)
    draw = ImageDraw.Draw(image)
    draw.text((40, 40), text, font=setFont, fill=fillColor, direction=None)
    image.save(filename)
    print('add title')
    # pic_text(filepath, size, text, setFont, fillColor, filename, direction=None)

def getDirs(path):
    for root, dirs, files in os.walk(path):
        return root, files

def generatePics():
    with open('stop_words.txt', 'rb') as f:
        stopWords = [line.decode('utf-8').replace('\r\n', '') for line in f.readlines()]

    root, files = getDirs('../txts/')
    for file in files:
        data = readfile(root+file)
        word_ist = jieba.cut(data)
        word_ist = [w for w in word_ist if w not in stopWords]
        word_str = " ".join(word_ist)
        word_cloud = wc.generate(word_str)
        print('generateWord')
        word_cloud.to_file('static/'+file[0:-4]+'.jpg')
        addTitle('static/'+file[0:-4]+'.jpg', file[0:-4], 'static/'+file[0:-4]+'.jpg')
        # plt.imshow(word_cloud)
        # plt.axis('off')
        # plt.show()

generatePics()


# wordList =  [w for w in wordList if len(w)>1
#  and not re.match('^[a-z|A-Z|0-9|.]*$', w) ]


# print(wordList)
# print(wordList)

# print(wordStr)

# tags = analyse.textrank(data, topK=30, withWeight=True)
# for i in tags:
#     print(i)