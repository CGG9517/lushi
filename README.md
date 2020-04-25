
# Title

本项目主要用于爬虫教学，炉石卡组爬取。

## Install

'''
import requests
from bs4 import BeautifulSoup
import re
import crawler.config as config
import os
import time
'''

## Usage

爬取地址：https://www.hearthstonetopdecks.com/decks/
配置文件：config.py
主程序：LuShiCrawler.py

主要使用技术：
1. 正则表达式，取url中的某段字符。
        正则：
            . 通配符
            + 代表1...n，默认贪婪模式
            * 代表0...n，默认贪婪模式
            {n,m} 代表n...m,
            ? 在+，*之后，表示非贪婪模式
            [] 里面值选择一个匹配
            () 括号优先，group取值时，group(0)代表原字符串，group(1)代表第一个括号内匹配的内容
            语法：https://www.jb51.net/tools/zhengze.html
            在线测试reg：https://regex101.com/
    
2. 使用bs4：
    参考地址：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#
        find：返回第一个匹配。 find("a", attrs={'class': 'page-link', 'rel': 'next'})
        find_all：返回匹配到的结果数组，方法同上。
        select：返回匹配到的结果数组，可以使用css选择器（推荐）。select('span.card-name')
                css选择器：
                    普通不带任何符号，代表tag名
                    . 后面跟一个class名（一个标签中可能包含多个class，使用空格隔开的，如<div class='content-area main-content'>）
                    # 后面跟id


## Contributing

jiangchao

## License
jiangchao

    