class Dist:
    def __init__(self, mt, ct):
        self.meters = mt
        self.centimeters = ct
        print("Работает конструктор")

    def get_dist(self):
        self.meters = int(input("Введите число метров:"))
        self.centimeters = float(input("Введите число сантиметров:"))

    def show_dist(self):
        print("{0} м {1} см".format(self.meters, self.centimeters))


dist1 = Dist(0, 0.0)
dist2 = Dist(14, 25.0)
dist3 = Dist(0, 0.0)
dist3.get_dist()

print("dist1 = ", end=" ")
dist1.show_dist()
print("dist2 = ", end=" ")
dist2.show_dist()
print("dist3 = ", end=" ")
dist3.show_dist()
