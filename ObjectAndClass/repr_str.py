# -*- encoding: utf-8 -*-


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair is (x:{0.x!r}, y:{0.y!r})'.format(self)

    # if __str__ haven't been defined. it will print __repr__ or __str__.
    def __str__(self):
        return '(x:{0.x!s}, y:{0.y!s})'.format(self)  # {0.y!s} == self.y and %s


if __name__ == '__main__':
    pair = Pair(1,2)
    print(pair)


