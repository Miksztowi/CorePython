# -*- encoding:utf-8 -*-
# __author__=='Gan'

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal total, count
        total += new_value
        count += 1
        return total / count
    return averager

if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))