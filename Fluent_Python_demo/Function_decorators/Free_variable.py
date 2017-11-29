# -*- encoding:utf-8 -*-
# __author__=='Gan'


def make_averager():

    # series = [0]
    series = []

    def averaher(new_value):
        series.append(new_value)
        # series[0] = 5  # Change the value of zero index.
        # series += new_value,
        # series = [1]
        total = sum(series)
        count = len(series)
        return total / count

    return averaher


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__[0].cell_contents)
