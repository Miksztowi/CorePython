# -*- encoding:utf-8 -*-
# __author__=='Gan'

from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def simple_generator():
    print(' coroutine start.')
    x = yield
    print(' coroutine received ', x)


if __name__ == '__main__':
    my_coro = simple_generator()
    print(getgeneratorstate(my_coro))
    print(my_coro.send(10))
