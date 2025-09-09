from bs4 import BeautifulSoup
from urllib.request import urlretrieve

import os
#获取当前脚本所在目录
_path = os.path.dirname(os.path.abspath(__file__))
def get_url(filename):
    if filename.endswith('1.html'):
        css='h2.post-title>a'
    else:
        css='ul.headline2>li[style]'
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one(css)
        #获取href属性
        if filename.endswith('2.html'):
            url = title.text.strip().split(' ')[-1]
            # urlretrieve(url,os.path.join(_path,'nodefile.txt'))
            urlretrieve(url,'nodefile.txt')
        else:
            url = title.attrs['href']
    return url
if __name__ == '__main__':
    # 获取命令行参数
    import sys
    if len(sys.argv)>1:
        filename = sys.argv[1]
    else:
        filename = 'shunfeng1.html'
    # filename = os.path.join(_path, filename)
    url = get_url(filename)
    print(url)

