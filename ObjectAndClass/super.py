# -*- encoding:utf-8 -*-
# __author__=='Gan'


class A:
    def spam(self):
        print('A.spam')
        super().spam()  # so it mean that A use spam() from B.

class B:
    def spam(self):
         print('B.spam')

class C(A,B):
    pass

if __name__ == '__main__':
    c = C()
    c.spam()

# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>,
# <class 'object'>)
# >>>
