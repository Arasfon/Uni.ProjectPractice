def calculate(x, y, a):
    """Вычисляет значение третьей ветки кусочно-заданной функции

    :param x: x
    :param y: y
    :param a: a
    :return: Значение ветки
    """
    m = x
    t2 = a
    t3 = y

    if t2 < m:
        m = t2

    if t3 < m:
        m = t3

    return m
