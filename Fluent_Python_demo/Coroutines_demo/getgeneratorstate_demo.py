# -*- encoding:utf-8 -*-
# __author__=='Gan'


from inspect import getgeneratorstate
def simple_coro2(a):
    print('-> started: a =', a)
    b = yield a
    print('-> received: b =', b)
    c = yield a + b
    print('-> received: c = ', c)

if __name__ == '__main__':
    my_coro2 = simple_coro2(10)
    print(getgeneratorstate(my_coro2))
    next(my_coro2)
    print(getgeneratorstate(my_coro2))
    my_coro2.send(20)
    print(getgeneratorstate(my_coro2))
    my_coro2.send(30)

