# -*- encoding:utf-8 -*-
# __author__=='Gan'


from collections import namedtuple

Result = namedtuple('result', 'count average')
def averager():
    total = count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(11)
    # print(coro_avg.send(None))

    try:
        coro_avg.send(None)
    except StopIteration as exec:
        print(exec.value)