class MyClass:
    pass


MyClass.x = 100
obj1, obj2 = MyClass(), MyClass()
obj1.y = 10
obj2.y = 20
print("obj1.x = {0} obj1.y = {1}".format(obj1.x, obj1.y))
print("obj2.x = {0} obj2.y = {1}".format(obj2.x, obj2.y))
