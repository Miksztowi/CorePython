# -*- encoding:utf-8 -*-
# __author__=='Gan'

import mmh3
from bitarray import bitarray

BIT_SIZE = 5000000


class BloomFilter:
    def __init__(self):
        # Initialize bloom filter, set size and all bits to 0
        self.bit_array = bitarray(BIT_SIZE)

    def add(self, url):
        point_list = self.get_postions(url)

        for i in point_list:
            self.bit_array[i] = 1

    def contains(self, url):
        point_list = self.get_postions(url)
        return all(self.bit_array[i] for i in point_list)

    def get_postions(self, url):
        point1 = mmh3.hash(url, 41) % BIT_SIZE
        point2 = mmh3.hash(url, 42) % BIT_SIZE
        point3 = mmh3.hash(url, 43) % BIT_SIZE
        point4 = mmh3.hash(url, 44) % BIT_SIZE
        point5 = mmh3.hash(url, 45) % BIT_SIZE
        point6 = mmh3.hash(url, 46) % BIT_SIZE
        point7 = mmh3.hash(url, 47) % BIT_SIZE

        return [point1, point2, point3, point4, point5, point6, point7]


if __name__ == '__main__':
    b = BloomFilter()
    print(b.add('https://www.cnblogs.com/cpselvis/p/6265825.html'))
    print(b.contains('https://www.cnblogs.com/cpselvis/p/6265825.html'))
    print(b.contains('http://blog.csdn.net/mxsgoden/article/details/8821936'))
    print(list(b.bit_array[i] for i in b.get_postions('https://www.cnblogs.com/cpselvis/p/6265825.html')))
    print(list(b.bit_array[i] for i in b.get_postions('http://blog.csdn.net/mxsgoden/article/details/8821936')))
