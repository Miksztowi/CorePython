# -*- encoding:utf-8 -*-
# __author__=='Gan'

from inspect import getgeneratorstate
class DemoException(Exception):
    """"An exception type for the  demonstration."""

def demo_exc_handling():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print('-> coroutine received: {!r}'.format(x))
    finally:
        print('Coroutine ending...')
    raise RuntimeError('This line should never run.')

if __name__ == '__main__':
    exc_coro = demo_exc_handling()
    next(exc_coro)

    # Demo 1
    # exc_coro.send(11)
    # exc_coro.send(22)
    # exc_coro.close()
    # print(getgeneratorstate(exc_coro))

    # Demo 2
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.throw(DemoException)
    print(getgeneratorstate(exc_coro))

    # Demo 3
    # exc_coro.send(11)
    # exc_coro.send(22)
    # exc_coro.throw(ZeroDivisionError)
    # print(getgeneratorstate(exc_coro))

