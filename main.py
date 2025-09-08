import requests
from urllib.parse import urlparse
from urllib.request import urlretrieve

import random
from bs4 import BeautifulSoup


def main():
    url1='https://skill-note.blogspot.com/search/label/Blogger'
    html1=requests.get(url1)
    if html1.status_code==200:
        print('获取页面成功')
        html1=html1.text
        soup1=BeautifulSoup(html1,'html.parser')
        item1=soup1.select('div.post-0 a')
        url2=item1[0].attrs['href']
        # url2='https://skill-note.blogspot.com/2023/06/bloggerfloat_67.html'
        print('获取链接',url2)
        html2=get_pagecontent(url2)
        soup2=BeautifulSoup(html2,'html.parser')
        item2=soup2.select('ul.headline2>li[style]')
        url3=item2[0].text.split(' ')[-2]
        print('获取节点文件',url3)
        nodefile='nodeslist-1.txt'
        urlretrieve(url3,nodefile)
        print('节点文件下载完成')
    else:
        print('获取页面失败')
if __name__ == '__main__':
    main()

