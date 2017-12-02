# -*- encoding:utf-8 -*-
# __author__=='Gan'


import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # reprlib.repr limits the generated string to 30 characters.


def gen_123():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    # s = Sentence('"The time has come," the Walrus said,')
    # print(s)
    # for word in s:
    #     print(word)
    # print(list(s))

    print(gen_123)
    print(gen_123())
    for i in gen_123():
        print(i)
    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
