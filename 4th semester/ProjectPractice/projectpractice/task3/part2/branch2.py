def calculate(x, y, a, b):
    """Вычисляет значение второй ветки кусочно-заданной функции

    :param x: x
    :param y: y
    :param a: a
    :param b: b
    :return: Значение ветки
    """
    m = x
    t2 = (x + y) / (x - y)
    t3 = (a + b - x) / 2

    if t2 > m:
        m = t2

    if t3 > m:
        m = t3

    return m
