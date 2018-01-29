# -*- encoding:utf-8 -*-
# __author__=='Gan'

one = 'one'
two = 'two'

# 01
print('%s %s' % (one, two))
print('{} {}'.format(one, two))

# This operation is not available with old-style formatting.
print('{1} {0}'.format(one, two))


# 02
class Data:
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


print('%s %r' % (Data(), Data()))
print('{!s} {!r}'.format(Data(), Data()))

# 03
# 右校准
print('%10s' % one)
print('{:>10}'.format(one))

# 左校准
print('%-10s' % one)
print('{:10}'.format(one))

# 自定义填充字符，下列操作在旧风格中均不可行。
print('{:_<10}'.format(one))
print('{:^10}'.format(one))  # 居中
print('{:^6}'.format('zip'))  # 居中操作中，遇到奇数分割的时候，会将多出来的填充位放在右边。

# 04
str_ = 'hello world.'
print('%.5s' % (str_))
print('{:.5}'.format(str_))

# 05
str_ = 'hello world.'
print('%10.5s' % str_)
print('{:>10.5}'.format(str_))

# 06
number_integer = 42
print('%d' % (number_integer))
print('{:d}'.format(number_integer))

number_float = 3.141592653589793
print('%f' % number_float)
print('{:f}'.format(number_float))

# 07
number_integer = 42
print('%4d' % number_integer)
print('{:4d}'.format(number_integer))

number_float = 3.141592653589793
print('%06.2f' % number_float)
print('{:06.2f}'.format(number_float))

# 08
number_integer = 42
print('%+d' % number_integer)
print('{:+d}'.format(number_integer))

# 09
# Negative
print('% d' % (- 23))
print('{: d}'.format(- 23))

print('{:=-5d}'.format(- 23))
print('{:=+5d}'.format(23))

# 10
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))

print('{first} {last}'.format(first='Hodor', last='Hodor!'))  # only available with new style formatting.

# 11
person = {'first': 'Jean-Luc', 'last': 'Picard'}
print('{p[first]} {p[last]}'.format(p=person))

data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))


class Plant(object):
    type = 'tree'


print('{p.type}'.format(p=Plant()))


class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]


print('{p.type}: {p.kinds[0][name]}'.format(p=Plant()))

# 12
from datetime import datetime

print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))

# 13
print('{:{align}{width}}'.format('test', align='>', width='10'))
print('{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3))
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))
print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))
from datetime import datetime
dt = datetime.now()
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
