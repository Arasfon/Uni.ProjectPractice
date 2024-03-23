from functions_module import calculate
from math import ceil, floor, trunc

try:
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
except ValueError:
    print("Некорректный ввод")
    exit()

try:
    result = calculate(x, y, a, b)
except ValueError:
    print("Некорректный ввод")
    exit()

print(f"Результат: {round(result, 3)}")
print(f"Результат (ceil): {ceil(result)}")
print(f"Результат (floor): {floor(result)}")
print(f"Результат (trunc): {trunc(result)}")

with open("result.txt", "w") as file:
    file.write(f"x: {x}\n")
    file.write(f"y: {y}\n")
    file.write(f"a: {a}\n")
    file.write(f"b: {b}\n")
    file.write(f"Результат: {round(result, 3)}\n")
    file.write(f"Результат (ceil): {ceil(result)}\n")
    file.write(f"Результат (floor): {floor(result)}\n")
    file.write(f"Результат (trunc): {trunc(result)}\n")
