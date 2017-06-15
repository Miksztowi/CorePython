# -*- coding:utf-8 -*-
import copy
from time import ctime
"""
计算机网络Rip协议实现。
"""


def bellman_ford(rip1, rip2, index_a, index_b):
    """
    根据bellman-ford算法更新当前路由表。
    :param rip1: 当前的router表
    :param rip2: 接受的router表
    :param index_a: 当前router的节点索引
    :param index_b: 接受的router的节点索引
    :return: 
    """
    r1 = copy.deepcopy(rip1)
    r2 = copy.deepcopy(rip2)
    r3 = []
    next_des = 'r{}'.format(index_b)
    print '{} before r{} update'.format(ctime(), index_a)
    print '-' * 30
    print r1
    print '-' * 30
    print 'r{} accept r{} router table'.format(index_a, index_b)
    for m, x in enumerate(r2):
        flag = 0
        for n, y in enumerate(r1):
            if x['des'] == y['des']:
                flag = 1
                if x['next'] == next_des:
                    x['len'] += 1
                    r1[n] = x
                    break
                else:
                    flag = 1
                    if x['len'] + 1 < y['len'] + x['len']:
                        x['len'] += 1
                        x['next'] = next_des
                        r1[n] = x
                        break
                    else:
                        break
                    # else:
                    #     r3.append(x)
        if flag == 0:
            x['len'] += 1
            x['next'] = next_des
            r1.append(x)
    print '{} after r{} update'.format(ctime(), index_a)
    print '-' * 30
    print r1
    print '-' * 30
    print '-' * 30
    print '-' * 30


def init_table(router_list):
    """
    初始化每一个router上的router表
    :param router_list: 
    :return: 
    """
    rip_table = []
    for i in xrange(len(router_list)):
        print "input the {} router list len".format(i)
        print "-"*30
        l = raw_input('>')
        temp_table = []
        for n in xrange(int(l)):
            print "-" * 30
            temp_table.append(raw_input('>'))
        rip_table.append(convert_rip_path(temp_table))
    return rip_table


def convert_rip_path(table):
    """
    将list接受的数据转化成dict。
    :param table: List存储的数据
    :return: 
    """
    rip_table = []
    for i in table:
        args_list = i.split(' ')
        rip_path = {'des': args_list[0], 'len': int(args_list[1]), 'next': args_list[2]}
        rip_table.append(rip_path)
    return rip_table


def get_network():
    """
    输入邻接矩阵
    :return: 
    """
    print '-'*30
    print 'input router number'
    router_num = raw_input('>')
    router_list = []
    print '-' * 30
    print 'input matrix'
    for i in xrange(int(router_num)):
        router_list.append(raw_input('>'))

    return router_list


def update_tables():
    """
    通过路由矩阵，判断路由器的连接关系。
    :return: 
    """
    router_list = get_network()
    table = init_table(router_list)
    for n, x in enumerate(router_list):
        for m, y in enumerate(x.split(' ')):
            if y == '1':
                bellman_ford(table[n], table[m], n+1, m+1)

if __name__ == '__main__':
    update_tables()