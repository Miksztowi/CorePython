# -*- encoding:utf-8 -*-
# __author__=='Gan'

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

def chain(*iterables):
    for it in iterables:
        yield from it

if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))
