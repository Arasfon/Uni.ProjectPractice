class MyClass:
    x = 10

    def __init__(self):
        self.y = 20


obj1, obj2 = MyClass(), MyClass()

print("obj1.x = {0} obj2.x = {1}".format(obj1.x, obj2.x))

MyClass.x = 50
print("obj1.x = {0} obj2.x = {1}".format(obj1.x, obj2.x))
print("obj1.y = {0} obj2.y = {1}".format(obj1.y, obj2.y))

obj1.y = 90
print("obj1.y = {0} obj2.y = {1}".format(obj1.y, obj2.y))

obj2.x = 60
MyClass.x = 80
print("obj1.x = {0} obj2.x = {1} MyClass.x = {2}".format(obj1.x, obj2.x, MyClass.x))
