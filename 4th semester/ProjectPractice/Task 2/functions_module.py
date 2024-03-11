from math import sin, sqrt


def calculate(x, y, a, b):
    r = 0

    if x > 0 and y > 0:
        r = a * sin(sqrt(x + y)) ** 2
    elif x > y:
        m = x
        t2 = (x + y) / (x - y)
        t3 = (a + b - x) / 2

        if t2 > m:
            m = t2

        if t3 > m:
            m = t3

        r = m
    else:
        m = x
        t2 = a
        t3 = y

        if t2 < m:
            m = t2

        if t3 < m:
            m = t3

        r = m

    return r
