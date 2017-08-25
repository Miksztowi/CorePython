# -*- coding:utf-8 -*-
__author__ = "ganbin"
import requests

def get(url ,proxy):
    r = requests.get(url, proxies=proxy, verify=False)
    return r.text


if __name__ == '__main__':
    proxy = {
            'http': 'http://49.81.254.120:8118',
            'https': 'https://14.221.237.5:8118'
        }
    url = 'https://test.amazonreviewinsight.com/api/tag/report/B005FEGYJC'
    print(get(url, proxy))





