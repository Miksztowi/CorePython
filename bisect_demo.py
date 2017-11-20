# -*- encoding:utf-8 -*-
# __author__=='Gan'
import bisect


# Searche Sorted List
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


# Other Examples.
def grade(score, breakpoints=[60, 70, 80, 90],grades='FDCBA'):
    return grades[bisect.bisect_right(breakpoints, score)]


# LeetCode
import bisect
class MyCalendar(object):
    def __init__(self):
        self.calendar = []
        self._start_sorted = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.calendar:
            self.calendar += (start, end),
            self._start_sorted += start,
            return True
        floor_index = bisect.bisect_left(self._start_sorted, start)
        if floor_index and self.calendar[floor_index - 1][1] > start:
                return False

        ceiling_index = bisect.bisect_right(self._start_sorted, start)
        if self.calendar[ceiling_index - 1][0] == start and self.calendar[ceiling_index - 1][0] < end:
                return False
        elif ceiling_index != len(self.calendar) and self.calendar[ceiling_index][0] < end:
                return False

        self.calendar.insert(floor_index, (start, end))
        self._start_sorted.insert(floor_index, start)
        return True


if __name__ == '__main__':
    print(grade(80))