from math import sin, sqrt


def calculate(x, y, a):
    """Вычисляет значение первой ветки кусочно-заданной функции

    :param x: x
    :param y: y
    :param a: a
    :return: Значение ветки
    """
    return a * sin(sqrt(x + y)) ** 2
