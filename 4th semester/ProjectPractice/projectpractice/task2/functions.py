from math import sin, sqrt


def calculate(x, y, a, b):
    """Вычисляет значение кусочно-заданной функции

    :param x: x
    :param y: y
    :param a: a
    :param b: b
    :return: Значение функции
    """
    r = 0

    if x > 0 and y > 0:
        print("Ветка 1: x > 0 и y > 0")

        r = a * sin(sqrt(x + y)) ** 2
    elif x > y:
        print("Ветка 2: x > y")

        m = x
        t2 = (x + y) / (x - y)
        t3 = (a + b - x) / 2

        if t2 > m:
            m = t2

        if t3 > m:
            m = t3

        r = m
    else:
        print("Ветка 3: иначе")

        m = x
        t2 = a
        t3 = y

        if t2 < m:
            m = t2

        if t3 < m:
            m = t3

        r = m

    return r
