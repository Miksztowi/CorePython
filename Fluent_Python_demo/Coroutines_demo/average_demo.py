# -*- encoding:utf-8 -*-
# __author__=='Gan'


def averager():
    total = count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coro_avg = averager()
    next(coro_avg)
    print(coro_avg.send(10))
    print(coro_avg.send(11))
    print(coro_avg.send(StopIteration))
    print(coro_avg.send(12))

    # coro_avg.close()
    # print(coro_avg.send(14))
