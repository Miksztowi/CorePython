# -*- encoding:utf-8 -*-
# __author__=='Gan'


def demo():
    s = 'ABC'
    for char in s:
        print(char)

    s = 'ABC'
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break


import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence(object):
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # reprlib.repr limits the generated string to 30 characters.

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
