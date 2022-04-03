#!/usr/bin/env python
from os import path
import os
import sys

LANG_LIST = [
    'zh',  # default language
    # 'zh_TW',
    'en',
    'ja',
]
POST_NAME = 'index'

root = path.dirname(__file__)
post_path = path.join(root, 'docs', sys.argv[1])

if sys.platform == 'win32':
    post_path = post_path.replace('/', '\\')
print('creating a new post in', post_path)


def get_postname(lang):
    return (POST_NAME if lang == 'zh' else POST_NAME+'.'+lang) + '.md'


for lang in LANG_LIST:
    filename = path.join(post_path, post_path, get_postname(lang))
    if not path.exists(post_path):
        os.makedirs(post_path)
    if not path.exists(filename):
        print('creating a post in', filename)
        with open(filename, "w", encoding="utf-8", newline='\n') as f:
            f.write('''---
title: 
---


''')
