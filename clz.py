def say():
    print("hello")


class Person:
    __age = 20

    @classmethod
    def cm(self):
        print("类方法")

    @staticmethod
    def sm():
        print('静态方法')

    def im(self):
        print("实例方法")

    def __init__(self, name, say):
        self.name = name
        self.say = say


Person.im("zhangsan")
p = Person("张三", say)
print(p.name)  # 张三
p.say()  # hello

# p = Person()
# p.name = "张三"
# print(p.name)  # 张三
# p.say = say
# p.say()  # hello

print(dir(Person))
print(dir(p))
print(dir())
