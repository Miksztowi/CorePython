# -*- coding:utf-8 -*-
__author__ = "ganbin"
import json
import csv

if __name__ == '__main__':
    with open('month.json', 'r')as f:
        data= json.loads(f.read())
    # fieldnames = ['month','value']
    # with open('data2.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for d in data['data'][0]['data']:
    #         writer.writerow({'month':d['month'], "value": d['value']}) # all
    fieldnames = ['month',"Automotive", "value"]
    with open('data3.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in data['data']['Automotive']:
            writer.writerow({'month':d['month'], "Automotive": d["name"], "value": d['value']}) # detail


    print(data)