
# Title

����Ŀ��Ҫ���������ѧ��¯ʯ������ȡ��

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

��ȡ��ַ��https://www.hearthstonetopdecks.com/decks/
�����ļ���config.py
������LuShiCrawler.py

��Ҫʹ�ü�����
1. ������ʽ��ȡurl�е�ĳ���ַ���
        ����
            . ͨ���
            + ����1...n��Ĭ��̰��ģʽ
            * ����0...n��Ĭ��̰��ģʽ
            {n,m} ����n...m,
            ? ��+��*֮�󣬱�ʾ��̰��ģʽ
            [] ����ֵѡ��һ��ƥ��
            () �������ȣ�groupȡֵʱ��group(0)����ԭ�ַ�����group(1)�����һ��������ƥ�������
            �﷨��https://www.jb51.net/tools/zhengze.html
            ���߲���reg��https://regex101.com/
    
2. ʹ��bs4��
    �ο���ַ��https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#
        find�����ص�һ��ƥ�䡣 find("a", attrs={'class': 'page-link', 'rel': 'next'})
        find_all������ƥ�䵽�Ľ�����飬����ͬ�ϡ�
        select������ƥ�䵽�Ľ�����飬����ʹ��cssѡ�������Ƽ�����select('span.card-name')
                cssѡ������
                    ��ͨ�����κη��ţ�����tag��
                    . �����һ��class����һ����ǩ�п��ܰ������class��ʹ�ÿո�����ģ���<div class='content-area main-content'>��
                    # �����id


## Contributing

jiangchao

## License
jiangchao

    