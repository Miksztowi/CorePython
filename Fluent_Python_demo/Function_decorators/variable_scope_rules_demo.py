# -*- encoding:utf-8 -*-
# __author__=='Gan'
import dis


def f1(a):
    print(a)
    print(b)


def f2(a):
    print(a)
    print(b)
    b = 9


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


if __name__ == '__main__':
    # b = 6
    # f1(3)
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)

