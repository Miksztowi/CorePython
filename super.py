# -*- coding:utf-8 -*-
__author__ = "ganbin"
class Base:
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        super.__init__(self)
        print('A.__init__')

class B(Base):
    def __init__(self):
        super.__init__(self)
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')

if __name__ == '__main__':
    print(C.__mro__)
