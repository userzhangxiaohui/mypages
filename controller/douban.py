import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}
content = []
def douban():
    url = 'https://www.douban.com/explore'
    html = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    articles = html.find('div', id="content").find_all('div', class_="item")
    for article in articles:
        img = article.find('img').get('src')
        title = article.find('div', class_="title").find('a').string
        url = article.find('div', class_="title").find('a').get('href')
        abst = article.find('div', class_="content").find_all('a')[1].string
        content.append({'img':img, 'title':title, 'url':url, 'abst':abst})
    with open(r'\Users\zhang\Desktop\python\learn\mypage\datas\douban.json', 'w') as fp:
        json.dump(content, fp=fp, indent=4, ensure_ascii=False)
    return content


if __name__ == '__main__':
    douban()
