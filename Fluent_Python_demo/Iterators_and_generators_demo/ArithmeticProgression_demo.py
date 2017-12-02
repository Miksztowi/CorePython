# -*- encoding:utf-8 -*-
# __author__=='Gan'

class ArithmeticProgression(object):
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

if __name__ == '__main__':
    ap1 = ArithmeticProgression(1, 0.5, 2)
    print(list(ap1))
    ap2 = ArithmeticProgression(1, 0.5)
    for i in ap2:
        print(i)
