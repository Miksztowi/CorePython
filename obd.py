# -*- coding:utf-8 -*-
__author__ = "ganbin"
import requests
import re
import csv
import json

def get(url):
    r = requests.get(url)
    return r.text
def clean_data(data):


    clean = re.sub(r'<p>', '', data)
    clean = re.sub(r'</p>', '', clean)
    clean = re.sub(r'<li>', '', clean)
    clean = re.sub(r'</li>', '', clean)
    clean = re.sub(r"<span id='ezoic-pub-ad-placeholder-109' class=\"ezoic-adpicker-ad\"></span>", '', clean)
    clean = re.sub(r"<span.+</span>", '', clean)
    clean = re.sub(r"<script.+script>", '', clean)
    clean = re.sub(r"<ul>", '', clean)
    clean = re.sub(r"</ul>", '', clean)
    clean = re.sub(r"<ol>", '', clean)
    clean = re.sub(r"</ol>", '', clean)
    clean = re.sub(r'<a href=\"/faq/what-is-bank-1-and-bank-2.php\">', '', clean)
    clean = re.sub(r'</a>', '', clean)
    clean = re.sub(r'Other camshaft DTC codes.+', '',clean)
    clean = re.sub(r'<div.+>?', '', clean)
    clean = re.sub(r'<div.+>?', '', clean)
    clean = re.sub(r'<a href=\"/(.)+\">?', '', clean)
    clean = re.sub(r'<p class.+>?', '', clean)
    clean = re.sub(r'<a href.+>?', '', clean)
    clean = re.sub(r'</*h3>?', '', clean)
    clean = re.sub(r'</*strong>', '', clean)
    if 'Please consult a factory service manual for more specific troubleshooting steps.' in data:
        clean = 'Please consult a factory service manual for more specific troubleshooting steps.'
    return clean

if __name__ == '__main__':
    with open('dtc.txt', 'r') as f:
        dtcs = f.readlines()
    re_d = re.compile('<h2>.*Diagnostic.*</h2>(.+)<div class="register">',
                      re.DOTALL | re.I | re.M)

    re_p = re.compile('<h2>.*Solutions.*</h2>(.+)<div class="register">',
                      re.DOTALL | re.I | re.M)

    with open('Possible_Solutions.csv', 'w') as f:
        field_names = ['DTC', 'Possible Solutions']
        csv_writer = csv.DictWriter(f, fieldnames=field_names)
        csv_writer.writeheader()
        for d in dtcs[1:200]:
            c = {}
            url = 'https://www.obd-codes.com/{}'.format(d.strip('\n '))
            content = get(url)
            solutions = re.search(re_p, content)
            if not solutions:
                solutions = re.search(re_d, content)
            from w3lib.html import  remove_tags
            solutions = remove_tags(solutions.group(1) if hasattr(solutions, 'group') else "")
            # solutions = clean_data(solutions.group(1) if hasattr(solutions, 'group') else "")
            csv_writer.writerow(
                {'DTC': d, 'Possible Solutions': solutions.encode('utf-8')})


            print(d, solutions)

