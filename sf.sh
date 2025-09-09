#!/bin/bash                                                                                                             
url1='https://skill-note.blogspot.com/search/label/Blogger'
curl -o shunfeng1.html $url1
url2=$(python3 main.py shunfeng1.html)
curl -o shunfeng2.html $url2
python3 main.py shunfeng2.html
