# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:46:04 2017

@author: lkj
"""

# -*- coding:utf-8 -*-
import codecs

import jieba
from scipy.misc import imread
from wordcloud import WordCloud


# 绘制词云
def save_jieba_result():
    # 设置多线程切割
    #jieba.enable_parallel(4)
    with codecs.open('comments.txt', encoding='utf-8') as f:
        comment_text = f.read()
    cut_text = " ".join(jieba.cut(comment_text))  # 将jieba分词得到的关键词用空格连接成为字符串
    with codecs.open('jieba.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)


def draw_wordcloud2():
    with codecs.open('jieba.txt', encoding='utf-8') as f:
        comment_text = f.read()

    color_mask = imread("zhanlang2.jpg")  # 读取背景图片,可以改为自己的

    stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是', u'什么', u'没有', u'这个', u'那个', u'大家', u'比较', u'看到', u'真是',
                 u'除了', u'时候', u'已经', u'可以',u'湄公河']
    #font_path需要指定，否则中文会乱码，这里用的是微软雅黑
    cloud = WordCloud(font_path="MSYH.TTF", background_color='white',
                      max_words=2000, max_font_size=200, min_font_size=4, mask=color_mask,stopwords=stopwords)
    word_cloud = cloud.generate(comment_text)  # 产生词云
    word_cloud.to_file("zhanlang2_cloud.jpg")

save_jieba_result()
draw_wordcloud2()