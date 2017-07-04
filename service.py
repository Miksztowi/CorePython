# -*- coding:utf-8 -*-
# import json
import hashlib
import hmac
import base64
import time
import json
import datetime
from collections import OrderedDict
from urllib import urlencode
from urlparse import urlsplit
from django.core.management.base import BaseCommand
import requests
from lxml import etree
from copy import deepcopy as cp
import time

SORTS = (
    'salesrank',
    'titlerank',
    'pmrank',
    'reviewrank'
)


class Command(BaseCommand):
    help = 'Parse amazon products info from specific category through Product Advertising API'
    base_params = {
        'AWSAccessKeyId': 'AKIAJLDNFJPQWTMBP2IA',
        'AssociateTag': 'topvc-20',
        'Operation': 'BrowseNodeLookup',
        'ResponseGroup': 'BrowseNodeInfo',
        'Service': 'AWSECommerceService',

    }
    AWSSecretKey = b'5mx8fQb2XRqj5Iplai7cHx7/3RD0eOrdka+6OTGZ'
    end_point = 'http://webservices.amazon.com/onca/xml'
    namespaces = {
        'xmlns': 'http://webservices.amazon.com/AWSECommerceService/2011-08-01'
    }
    tasks = {}
    done_tasks = []
    price_step = 10
    root_name = ''

    def make_request(self, id_params):
        signed_params = self.prepare_query_params(id_params)
        try:
            r = requests.get(self.end_point, params=signed_params)
        except Exception as e:
            print(str(e))
            import pdb
            pdb.set_trace()
            return True
        if r.status_code != requests.codes.ok:
            print(r.status_code)
            if r.status_code == 503:
                print(id_params)
                time.sleep(1)
                key = self.gen_task_key(id_params)
                if key in self.done_tasks:
                    self.done_tasks.remove(key)
                self.gen_new_task(id_params)
                return False
            import pdb
            pdb.set_trace()
            return False
        return r

    def run_task(self, children_id):
        namespaces = {
            'xmlns': 'http://webservices.amazon.com/AWSECommerceService/2011-08-01'
        }
        r = self.make_request(children_id)
        if not r:
            return False
        tree = etree.XML(r.content.decode(r.encoding or 'utf8'))
        # if node_depth == 0:
        #     root_name = tree.xpath('node()[2]/*[1]//*/text()')
        # node_depth += 1
        has_children = tree.findall('.//xmlns:BrowseNodes/xmlns:BrowseNode/xmlns:Children', namespaces)

        if has_children:
            children = tree.xpath('node()[2]/*[2]/*[3]//*/text()')
            for i in children[::2]:
                children_id['BrowseNodeId'] = i
                time.sleep(1)
                self.run_task(children_id)
        else:
            leaf_node = tree.xpath('node()[2]/*[1]//*/text()')
            leaf_node.append('Automotive')
            with open('leaf_node.txt', 'a') as f:
                f.write(json.dumps(leaf_node)+'\n')

            return

    def prepare_query_params(self, id_params):
        params = self.base_params.copy()
        params.update(id_params)
        if 'price_step' in params.keys():
            del params['price_step']
        now = datetime.datetime.utcnow()
        timestamp = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        params['Timestamp'] = timestamp
        ordered_params = OrderedDict(
            sorted(params.items(), key=lambda t: t[0]))
        # print(ordered_params)
        query = urlencode(ordered_params).replace('+', '%20')
        sp = urlsplit(self.end_point)
        sign_str = '\n'.join(('GET', sp.netloc, sp.path, query))
        # print(sign_str)
        sign = base64.b64encode(hmac.new(
            self.AWSSecretKey, msg=sign_str,
            digestmod=hashlib.sha256).digest())
        ordered_params['Signature'] = sign
        return ordered_params


if __name__ == '__main__':
    c = Command()
    id_params = {'BrowseNodeId': '15684181'}

    print c.run_task(id_params)
