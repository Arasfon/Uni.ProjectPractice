import branch1
import branch2
import branch3


class PiecewiseFunction:
    """Класс для хранения значений аргументов и вычисления значения кусочно-заданной функции"""

    def __init__(self, x, y, a, b):
        print("Работает конструктор")

        self.x = x
        self.y = y
        self.__a = a
        self.__b = b

    @property
    def a(self):
        return self.__a

    def read_arguments_from_stdin(self):
        """Считывает аргументы функции с стандартного потока ввода"""
        self.x = float(input("Введите x: "))
        self.y = float(input("Введите y: "))
        self.__a = float(input("Введите a: "))
        self.__b = float(input("Введите b: "))

    def __calculate_branch1(self):
        """Вычисляет значение первой ветки

        :return: Значение первой ветки
        """
        return branch1.calculate(self.x, self.y, self.__a)

    def __calculate_branch2(self):
        """Вычисляет значение второй ветки

        :return: Значение второй ветки
        """
        return branch2.calculate(self.x, self.y, self.__a, self.__b)

    def __calculate_branch3(self):
        """Вычисляет значение третьей ветки

        :return: Значение третьей ветки
        """
        return branch3.calculate(self.x, self.y, self.__a)

    def calculate(self):
        if self.x > 0 and self.y > 0:
            print("Ветка 1: x > 0 и y > 0")
            result = self.__calculate_branch1()
        elif self.x > self.y:
            print("Ветка 2: x > y")
            result = self.__calculate_branch2()
        else:
            print("Ветка 3: иначе")
            result = self.__calculate_branch3()
        return result


current_menu_option = None
while current_menu_option != "0":
    print("Меню")
    print("0 — Выйти")
    print("1 — Выполнить программу")

    current_menu_option = input("Выберите пункт меню: ")

    if current_menu_option == "0":
        print("Завершение работы")
    elif current_menu_option == "1":
        function = PiecewiseFunction(0, 0, 0, 0)
        function.read_arguments_from_stdin()

        result = function.calculate()

        print(f"Результат: {round(result, 3)}")
    else:
        print("Такого пункта меню не существует")

    print()
