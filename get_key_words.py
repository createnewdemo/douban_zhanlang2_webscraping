# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:51:51 2017

@author: lkj
"""
import codecs
import jieba
import matplotlib.pyplot as plt  
import matplotlib as mpl 
import numpy as np 
from collections import Counter

zhfont1 = mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

def draw_bar(labels,quants):  
    width = 0.4  
    ind = np.linspace(0.5,9.5,10)  
    # make a square figure  
    fig = plt.figure(1)  
    ax  = fig.add_subplot(111)  
    # Bar Plot  
    ax.bar(ind-width/2,quants,width,color='green')  
    # Set the ticks on x-axis  
    ax.set_xticks(ind)  
    ax.set_xticklabels(labels,fontproperties=zhfont1)  
    # labels  
    ax.set_xlabel(u'关键词',fontproperties=zhfont1)  
    ax.set_ylabel(u'评论数量',fontproperties=zhfont1)  
    # title  
    ax.set_title(u'筛选后的TOP10关键词', bbox={'facecolor':'0.8', 'pad':5},fontproperties=zhfont1)  
    #plt.legend(prop=zhfont1)
    plt.grid(True)  
    plt.show()   

word_lists = []  # 关键词列表
with codecs.open('comments.txt', 'r', encoding='utf-8') as f:
    Lists = f.readlines()  # 文本列表
    for List in Lists:
        cut_list = list(jieba.cut(List))
        for word in cut_list:
            word_lists.append(word)
word_lists_set = set(word_lists)  # 去除重复元素
sort_count = []
word_lists_set = list(word_lists_set)
length = len(word_lists_set)
print(u"共有%d个关键词" %length)
k = 1
for w in word_lists_set:
    sort_count.append(w + u':' + str(word_lists.count(w)) + u"次\n")
    print (u"%d---" % k + w + u":" + str(word_lists.count(w)) + u"次")
    k += 1
with codecs.open('count_word.txt', 'w', encoding='utf-8') as f:
    f.writelines(sort_count)
#先取出前100关键词，再进行人为筛选
key_words_TOP100=[]
key_words_TOP100=Counter(word_lists).most_common(100)
key_words_shaixuan=[key_words_TOP100[6],key_words_TOP100[24],key_words_TOP100[25],
                    key_words_TOP100[30],key_words_TOP100[39],key_words_TOP100[52],
                    key_words_TOP100[60],key_words_TOP100[77],key_words_TOP100[78],
                    key_words_TOP100[94]]
labels = []
quants = []
for i in range(10):
    labels.append(key_words_shaixuan[i][0])
    quants.append(key_words_shaixuan[i][1])
draw_bar(labels,quants)