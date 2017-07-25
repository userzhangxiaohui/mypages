# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json

#设置headers
headers = {
    'referer': 'http://jandan.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}

content = []
#获取所有首页文章节点
def get_articles():
    url = 'http://jandan.net'
    html = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    articles = html.find('div', id="content").find_all('div', class_='list-post')
    for article in articles:
        url = article.find('a').get('href')
        title = article.find_all('a')[1].string
        content.append({'title':title,'href':url})
    with open(r'\Users\zhang\Desktop\python\learn\mypage\datas\jandan.json','w') as fp:
        json.dump(content, fp=fp, indent=4, ensure_ascii=False)
    return content[0:16]

def get_pics():
    url = 'http://jandan.net/pic'
    html = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    pics = html.find_all('a', class_='view_img_link', limit=3)
    content = []
    for pic in pics:
        url = pic.get('href')
        content.append({'img':url})
    return content

if __name__ =='__main__':
    print(get_pics())