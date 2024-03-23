def triangle_area(x1, y1, x2, y2, x3, y3):
    """
    Вычисляет площадь треугольника
    :param x1: Абсцисса первой точки
    :param y1: Ордината первой точки
    :param x2: Абсцисса второй точки
    :param y2: Ордината второй точки
    :param x3: Абсцисса третьей точки
    :param y3: Ордината третьей точки
    :return: Значение площади треугольника
    """
    return 1.0 / 2 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))


def pentagon_area(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    """
    Вычисляет площадь пятиугольника
    :param x1: Абсцисса первой точки
    :param y1: Ордината первой точки
    :param x2: Абсцисса второй точки
    :param y2: Ордината второй точки
    :param x3: Абсцисса третьей точки
    :param y3: Ордината третьей точки
    :param x4: Абсцисса четвёртой точки
    :param y4: Ордината четвёртой точки
    :param x5: Абсцисса пятой точки
    :param y5: Ордината пятой точки
    :return: Значение площади пятиугольника
    """
    return triangle_area(x1, y1, x2, y2, x3, y3) + triangle_area(x1, y1, x3, y3, x4, y4) + triangle_area(x1, y1, x4, y4, x5, y5)


try:
    x1, y1 = map(float, input("Введите координаты первой точки, разделяя их пробелом: ").split())
    x2, y2 = map(float, input("Введите координаты второй точки, разделяя их пробелом: ").split())
    x3, y3 = map(float, input("Введите координаты третьей точки, разделяя их пробелом: ").split())
    x4, y4 = map(float, input("Введите координаты четвёртой точки, разделяя их пробелом: ").split())
    x5, y5 = map(float, input("Введите координаты пятой точки, разделяя их пробелом: ").split())
except ValueError:
    print("Некорректный ввод")
    exit()

try:
    result = pentagon_area(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
except ZeroDivisionError:
    print("Некорректный ввод — все числа не должны быть равны нулю")
    exit()

print(f"Площадь пятиугольника с заданными точками равна {result:.3f}")

try:
    with open("task1_output.txt", "w", encoding="utf-8") as file:
        file.write(f"Координаты первой точки: ({x1}, {y1})\n")
        file.write(f"Координаты второй точки: ({x2}, {y2})\n")
        file.write(f"Координаты третьей точки: ({x3}, {y3})\n")
        file.write(f"Координаты четвёртой точки: ({x4}, {y4})\n")
        file.write(f"Координаты пятой точки: ({x5}, {y5})\n")
        file.write("\n")
        file.write(f"Площадь пятиугольника с заданными точками равна {result:.3f}\n")
except OSError:
    print("Ошибка записи в файл")
    raise
