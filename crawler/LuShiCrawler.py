import requests
from bs4 import BeautifulSoup
import re
import crawler.config as config
import os
import time


def download_list(_url: str, _file_path):
    """
    使用递归方式获取列表，存储成文件
    :param _file_path: 存储路径
    :param _url: 开始页面url
    :return:
    """
    # 使用正则取url的页码
    reg1 = re.compile(r'^http(s)?:\/\/[a-zA-z0-9.\/]+?\/page\/(\d+)')
    match_res = reg1.search(_url)
    _page_num = 1
    if match_res:
        _page_num = match_res.group(2)

    _resp = requests.get(_url, headers=config.headers)
    _soup = BeautifulSoup(_resp.text, 'lxml')

    _deck_list_tag = _soup.select('table#deck-list')
    if _deck_list_tag:
        # <h4> list
        _h4_list = _deck_list_tag[0].select("h4")
        if _h4_list:
            with open(_file_path, 'a', encoding='UTF-8') as _f:
                _url_count = 0
                for _h4_tag in _h4_list:
                    _a_tag = _h4_tag.find("a")  # <a>
                    if _a_tag:
                        _href = _a_tag.get('href')
                        _f.write(_href + '\n')
                        _url_count += 1
                _f.flush()
                print('download [{}] page {} urls.'.format(_page_num, _url_count))
    #  next page
    _next_button = _soup.find("a", attrs={'class': 'page-link', 'rel': 'next'})

    if _next_button:
        _next_url = _next_button.get('href')
        if _next_url:
            download_list(_next_url, _file_path)


def download_deck(_url, _file_path, _count):
    _resp = requests.get(_url, headers=config.headers)
    _soup = BeautifulSoup(_resp.text, 'lxml')

    # 使用正则取url中包含的卡组命名
    reg2 = re.compile(r'^http(s)?:\/\/[a-zA-z0-9.\/]+?\/decks\/([a-zA-z\-0-9]+)')
    reg_res = reg2.search(_url)
    _deck_name = '无名卡组'
    if reg_res:
        _deck_name = reg_res.group(2)  # 卡组名字

    # 卡组列表
    card_frame_list = _soup.select('li.card-frame')
    if card_frame_list:
        with open(_file_path, 'a', encoding='UTF-8') as _f:
            _f.write('[{}]\n'.format(_deck_name))
            for card_frame in card_frame_list:
                name_tag = card_frame.select('span.card-name')
                cost_tag = card_frame.select('span.card-cost')
                count_tag = card_frame.select('span.card-count')

                card_name = name_tag[0].get_text()  # 卡名
                card_cost = cost_tag[0].get_text()  # 卡费
                card_count = count_tag[0].get_text()  # 数量
                _f.write('\t{}, {}, {}\n'.format(card_name, card_cost, card_count))
            _f.write('\n')
            _f.flush()
            print('下载第[{}]套卡组成功！'.format(_count))


if __name__ == '__main__':

    # 卡组链接保存地址
    deck_url = "../resource/deck_url.txt"

    # 卡组信息保存地址
    _deck_frame_path = '../resource/deck_frame.txt'

    # 首先删除存储文件
    if os.path.exists(deck_url):
        os.remove(deck_url)
    if os.path.exists(_deck_frame_path):
        os.remove(_deck_frame_path)

    # 构建新文件
    os.makedirs(os.path.dirname(deck_url), exist_ok=True)
    os.makedirs(os.path.dirname(_deck_frame_path), exist_ok=True)

    # 下载所有卡组url
    download_list(config.start_url, deck_url)

    # 遍历url下载所有卡组
    with open(deck_url, 'r') as f:
        i = 0
        for line in f:
            i += 1
            download_deck(line.strip(), _deck_frame_path, i)
