# -*- encoding:utf-8 -*-
# __author__=='Gan'


def simple_generator():
    print(' coroutine start.')
    x = yield
    print(' coroutine received ', x)


if __name__ == '__main__':
    my_coro = simple_generator()
    print(my_coro)
    # next(my_coro)
    my_coro.send(0)