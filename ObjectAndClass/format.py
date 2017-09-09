# -*- encoding:utf-8 -*-
# __author__ == 'Gan'

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}',
}


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


if __name__ == '__main__':
    date = Date(2017, 9, 9)
    print(format(date, 'mdy'))
    print('Today is {:ymd}'.format(date))


    print('Today is {:aa}'.format(date))
    # Traceback (most recent call last):
    #   File "/Users/wukong/Python/Git/CorePython/ObjectAndClass/format.py", line 28, in <module>
    #     print('Today is {:aa}'.format(date))
    #   File "/Users/wukong/Python/Git/CorePython/ObjectAndClass/format.py", line 20, in __format__
    #     fmt = _formats[format_spec]
    # KeyError: 'aa'
    # after debugger. i think {:ymd} and format(date, 'ymd') are equal,but it would be useful after rewrite __format__.


