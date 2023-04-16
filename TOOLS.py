# 导入模块
import time
import requests
from lxml import etree


# 请求头函数
def headers_random():
    import random
    headers_list = [
        'Mozilla/5.0.html (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.html.2171.71 '
        'Safari/537.36',
        'Mozilla/5.0.html (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.html.1271.64 '
        'Safari/537.11',
        'Mozilla/5.0.html (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) '
        'Chrome/10.0.html.648.133 Safari/534.16',
        'Mozilla/5.0.html (Windows NT 6.1; WOW64; rv:34.0.html) Gecko/20100101 Firefox/34.0.html',
        'Mozilla/5.0.html (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) '
        'Firefox/3.6.10'
    ]
    headers = {
        'User-Agent': random.choice(headers_list)
    }
    return headers


# 获取网页树
def get_tree(url, headers=None, mode='get', params=None, proxies=None, verify=True):
    if mode == 'get' or mode == 'GET':
        resp = requests.get(url=url, headers=headers, params=params, proxies=proxies, verify=verify)
        resp.encoding = resp.apparent_encoding
        tree = etree.HTML(resp.text)
        time.sleep(2)
        return tree


# 获取美丽汤
def get_soup(url, headers=None, mode='get', params=None, proxies=None, verify=True):
    from bs4 import BeautifulSoup
    if mode == 'get' or mode == 'GET':
        resp = requests.get(url=url, headers=headers, params=params, proxies=proxies, verify=verify)
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, 'lxml')
        time.sleep(2)
        return soup


# 获取二进制数据
def get_content(url, headers=None, mode='get', params=None, proxies=None, verify=True):
    if mode == 'get' or mode == 'GET':
        resp = requests.get(url, headers=headers, params=params, proxies=proxies, verify=verify)
        content = resp.content
        time.sleep(2)
        return content


# 获取目标数据
def get_data(tree, rule='//text()'):
    data = tree.xpath(rule)
    return data


# 创建文件夹
def get_path(path='./Downloads'):
    import os
    if not os.path.exists(path):
        if path[-4] != '.' and path[-5] != '.':
            os.mkdir(path)
        else:
            open_file(path, mode='w')
    return path


# 文件操作函数
def open_file(into, mode='r', data=None, encoding='utf-8'):
    if mode == 'r':
        with open(into, mode='r', encoding=encoding) as f:
            return f.read()
    elif mode == 'rl':
        with open(into, mode='r', encoding=encoding) as f:
            return f.readline()
    elif mode == 'rs':
        with open(into, mode='r', encoding=encoding) as f:
            return f.readlines()
    elif mode == 'a':
        with open(into, mode='a', encoding=encoding) as f:
            f.write(str(data))
            f.write('\n')
    elif mode == 'al':
        with open(into, mode='a', encoding=encoding) as f:
            for dt in data:
                f.write(str(dt))
                f.write('\n')
    elif mode == 'wb':
        with open(into, mode='wb') as f:
            f.write(data)
    else:
        with open(into, mode='w', encoding=encoding) as f:
            if data:
                f.write(str(data))
            else:
                f.write('')
    return None


# 主程序入口
if __name__ == "__main__":
    pass
