# -*- coding:utf-8 -*-
__author__ = "ganbin"
import subprocess
import requests
import json
import re

if __name__ == '__main__':
    # subprocess.call(' curl -x http://103.78.143.250:8080 https://httpbin.org/get\?show_env\=1', shell=True)

    # proxies = {
    #     "https": "http://103.245.77.56:8080/",
    #     # "http": "http://103.78.143.250:8080/",
    # }
    # url = 'https://httpbin.org/get?show_env=1'
    # # url = 'http://www.vpngate.net/cn/'
    # r = requests.get(url, proxies=proxies)
    # print(r.content)
    with open('data/validated_proxies.txt', 'r') as f:
        rf = f.readlines()
    proxies = [x.strip('\n') for x in rf]
    temp_proxies = map(lambda x: re.sub(' ', ':', x), proxies)
    https_proxies = [x for x in temp_proxies]

    with open('data/validated_proxies.txt', 'w') as f:
        json.dump(https_proxies, f)

