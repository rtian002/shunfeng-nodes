#!/bin/bash                                                                                                             
url1='https://skill-note.blogspot.com/search/label/Blogger'
curl -so shunfeng1.html $url1
sleep 5
ls -l
url2=$(python3 main.py shunfeng1.html)
curl -so shunfeng2.html $url2
sleep 5
ls -l
python3 main.py shunfeng2.html
