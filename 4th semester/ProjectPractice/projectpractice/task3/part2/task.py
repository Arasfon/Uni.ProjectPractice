import branch1
import branch2
import branch3


class PiecewiseFunction:
    """Класс для хранения значений аргументов и вычисения значения кусочно-заданной функции"""

    def __init__(self, x, y, a, b):
        print("Работает конструктор")

        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def read_arguments_from_stdin(self):
        """Считывает аргументы функции с стандартного потока ввода"""
        self.x = float(input("Введите x: "))
        self.y = float(input("Введите y: "))
        self.a = float(input("Введите a: "))
        self.b = float(input("Введите b: "))

    def calculate_branch1(self):
        """Вычисляет значение первой ветки

        :return: Значение первой ветки
        """
        return branch1.calculate(self.x, self.y, self.a)

    def calculate_branch2(self):
        """Вычисляет значение второй ветки

        :return: Значение второй ветки
        """
        return branch2.calculate(self.x, self.y, self.a, self.b)

    def calculate_branch3(self):
        """Вычисляет значение третьей ветки

        :return: Значение третьей ветки
        """
        return branch3.calculate(self.x, self.y, self.a)


function = PiecewiseFunction(0, 0, 0, 0)
function.read_arguments_from_stdin()

result = 0

if function.x > 0 and function.y > 0:
    print("Ветка 1: x > 0 и y > 0")
    result = function.calculate_branch1()
elif function.x > function.y:
    print("Ветка 2: x > y")
    result = function.calculate_branch2()
else:
    print("Ветка 3: иначе")
    result = function.calculate_branch3()

print(f"Результат: {round(result, 3)}")
