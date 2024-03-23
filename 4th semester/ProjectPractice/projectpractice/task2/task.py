from math import ceil, floor, trunc
from .functions import calculate
from .errors import FormatError

import logging

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s", filename="task2_log.log", encoding="utf8", level=logging.DEBUG)

try:
    try:
        x = float(input("Введите x: "))
        y = float(input("Введите y: "))
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
    except ValueError as err:
        raise FormatError("Некорректный формат входных данных")

    result = calculate(x, y, a, b)

    print(f"Результат: {round(result, 3)}")
    print(f"Результат (с округлением): {round(result)}")
    print(f"Результат (с округлением вверх): {ceil(result)}")
    print(f"Результат (с округлением вниз): {floor(result)}")
    print(f"Результат (без дробной части): {trunc(result)}")

    with open("task2_output.txt", "w") as file:
        file.write(f"x: {x}\n")
        file.write(f"y: {y}\n")
        file.write(f"a: {a}\n")
        file.write(f"b: {b}\n")
        file.write(f"Результат: {round(result, 3)}\n")
        file.write(f"Результат (с округлением): {round(result)}\n")
        file.write(f"Результат (с округлением вверх): {ceil(result)}\n")
        file.write(f"Результат (с округлением вниз): {floor(result)}\n")
        file.write(f"Результат (без дробной части): {trunc(result)}\n")
except Exception as ex:
    str_ex = str(ex)
    print(str_ex)
    with open("task2_output.txt", "w") as file:
        file.write(f"Произошла ошибка: {str_ex}")
    logging.critical(str_ex, exc_info=True)
