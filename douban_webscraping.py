"""
 -*- coding: utf-8 -*-
 @author: Kaijian Liu
 @email:kaijianliu@qq.com
"""

import requests
from bs4 import BeautifulSoup
import codecs
import time

absolute_url = 'https://movie.douban.com/subject/26363254/comments'
url = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}




def html_prase(html, struct):
    soup=BeautifulSoup(html,'lxml')
    comment_nodes = []
    comment_nodes = soup.select(struct)
    xiangdui_link_nodes= soup.select('#paginator > a')[0].get('href')
    return comment_nodes,xiangdui_link_nodes

if __name__ == '__main__':
    f_cookies = open('cookie.txt', 'r')
    cookies = {}
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    f = codecs.open("comments.txt", 'a', encoding='utf-8')
    html = requests.get(url, cookies=cookies, headers=header).content
    comment_nodes=[]
    xiangdui_links=[]
    comment_nodes,xiangdui_link_nodes = html_prase(html , '.comment > p')
    soup = BeautifulSoup(html, 'lxml')
    comment_list = []
    for node in comment_nodes:
        comment_list.append(node.get_text().strip().replace("\n", "") + u'\n')
    while(xiangdui_link_nodes!=[]):
        xiangdui_link = soup.select('#paginator > a')[0].get('href')
        xiangdui_links.append(xiangdui_link)
        time.sleep(1)
        html = requests.get(absolute_url+xiangdui_link_nodes, cookies=cookies, headers=header).content
        soup = BeautifulSoup(html, 'lxml')
        comment_nodes, xiangdui_link_nodes = html_prase(html, '.comment > p')
        for node in comment_nodes:
            comment = node.get_text().strip().replace("\n", "") + u'\n'
            comment_list.append(comment)
            f.writelines(comment)

