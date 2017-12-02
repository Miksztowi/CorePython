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
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # reprlib.repr limits the generated string to 30 characters.


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
