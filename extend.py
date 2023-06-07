class Father:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("hello")


class Son(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say(self):
        super().say()
        print("world")


print(dir(object))
