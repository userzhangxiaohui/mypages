import json
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}

#生成目录
def get_directory():
    pass

def get_post(url):
    html = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    contents = html.find('div', id="content").find_all('p')
    post = ''
    for content in contents:
        post += content.string
        post += '\n'
    return post



def fictionread(number):
    with open(r'\Users\zhang\desktop\python\learn\mypage\datas\taiyangdejuli.json', 'r') as fp:
        fictions = json.load(fp)
    number = int(number) - 1
    title = fictions[number]['title']
    url = fictions[number]['href']
    post = get_post(url)
    next_href = '/fiction/' + str(number+2)
    prev_href = '/fiction/' + str(number)
    if int(number) == 1 or int(number) == 0:
        prev_href = '/fiction/1'
    return title,post,prev_href, next_href

if __name__ == "__main__":
    print(fictionread(3))