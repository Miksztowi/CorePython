# -*- encoding:utf-8 -*-
# __author__=='Gan'

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end.')


import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # reprlib.repr limits the generated string to 30 characters.


if __name__ == '__main__':
    # res1 = [x*3 for x in gen_AB()]
    # for i in res1:
    #     print(i)
    # res2 = (x*3 for x in gen_AB())
    # for i in res2:
    #     print(i)

    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
