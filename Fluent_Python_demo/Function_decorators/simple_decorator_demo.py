# -*- encoding:utf-8 -*-
# __author__=='Gan'

import time
import functools


def clock(func):
    series = []

    def clocked(*args):
        t0 = time.perf_counter()
        series.append(func)
        _result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s (%s) -> %r ' % (elapsed, name, arg_str, _result))
        return _result

    return clocked

def clock(func):
    series = []
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        series.append(func)
        _result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s (%s) -> %r ' % (elapsed, name, arg_str, _result))
        return _result

    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(0.123)')
    snooze(.123)
    print(snooze.__name__)
