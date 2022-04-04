#!/usr/bin/env python
from os import path
import os
import sys

LANG_LIST = [
    'zh',  # default language
    # 'zh_TW',
    'en',
    # 'ja',
]
POST_NAME = 'index'


def get_postname(lang):
    return (POST_NAME if lang == 'zh' else POST_NAME+'.'+lang) + '.md'


def create_post():
    root = path.dirname(__file__)
    relative_path = path.join('docs', sys.argv[1])
    post_path = path.join(root, relative_path)

    if sys.platform == 'win32':
        relative_path = relative_path.replace('/', '\\')
        post_path = post_path.replace('/', '\\')

    for lang in LANG_LIST:
        postname = get_postname(lang)
        filename = path.join(post_path, postname)
        if not path.exists(post_path):
            os.makedirs(post_path)
        if not path.exists(filename):
            print('creating a post in',  path.join(relative_path, postname))
            with open(filename, "w", encoding="utf-8", newline='\n') as f:
                f.write('''---
title: 
---


''')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('''eg.
$ python new.py game-guides/some-skills
> creating a new post in docs/game-guides/some-skills/index.md
> creating a new post in docs/game-guides/some-skills/index.xxx.md
''')
    else:
        create_post()
