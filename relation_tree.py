# -*- coding:utf-8 -*-
__author__ = "ganbin"
from django.http import JsonResponse
from amazon.models import AmazonCategory
from amazon.utils import l, enqueue
import json
import time
from datetime import datetime
from functools import wraps
from django.core.management.base import BaseCommand
from django_redis import get_redis_connection
import django_rq
import logging


redis_con = get_redis_connection("default")



class Command(BaseCommand):
    redis_con = get_redis_connection("default")
    id_dict = {}
    parent_id_dict = {}


    def handle(self, *args, **options):
        global id_dict
        global parent_id_dict
        categorynodes = {
            'Electronics': 172282,
            # 'HomeGarden': 1055398,
            # 'Beauty': 3760911,
            # 'Baby': 165793011,
            # 'SportingGoods': 3375251,
            'Automotive': 15684181,
        }
        relation_list = []
        for k,v in categorynodes.items():
            searchindex= AmazonCategory.objects.filter(search_index=k)
            for s in searchindex:
                self.id_dict[s.id] = s
                if s.parent_id:
                    if self.parent_id_dict.get(s.parent_id):
                        self.parent_id_dict[s.parent_id].append(s.id)
                    else:
                        self.parent_id_dict[s.parent_id] = [s.id]

            for i in self.id_dict:
                if (self.id_dict[i].parent_id is None) and (self.id_dict[i].title == k) :
                    root_id = self.id_dict[i].id
                else:
                    continue
            relation_tree =  self._recursion(parent=root_id)
            relation_list.append(relation_tree)

        # print("cost %s " % (datetime.now()-now))
        print(relation_list)
        return {'data': '1'}



    def _recursion(self, parent):

        id = parent
        title = self.id_dict[parent].title
        parent_dict = {'id':id, 'name':title}
        child_tree = []
        try:
            children_list = self.parent_id_dict[parent]
        except:
            children_list = []
        if len(children_list) > 0:
            for child in children_list:
                child_dict = {}
                child_dict['id'] = child
                child_dict['name'] = self.id_dict[child].title

                child_tree.append(self._recursion(child))
        if child_tree:
            parent_dict['children'] = child_tree
        return parent_dict

