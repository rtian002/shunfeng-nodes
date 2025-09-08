import requests
from urllib.parse import urlparse
from urllib.request import urlretrieve

import random
from bs4 import BeautifulSoup

def get_pagecontent(url, type='text'):
    my_headers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"]  # ----请求页面,添加头信息,规避403页面(反爬)
    host = urlparse(url).netloc
    header = {"User-Agent": random.choice(my_headers), "Host": host, "Origin": f"https://{host}",
              "Referer": f"https://{host}/"}
    try:
        response = requests.get(url, headers=header, timeout=3)
        if response.status_code == 200:
            response.encoding = "utf-8"
            if type == 'json':
                page_content = response.json()
            else:
                page_content = response.text
            return page_content  # 网页内容，文本
        else:
            return None
    except requests.exceptions.RequestException:
        pass
    return None

def main():
    url1='https://skill-note.blogspot.com/search/label/Blogger'
    html1=get_pagecontent(url1)
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
if __name__ == '__main__':
    main()
