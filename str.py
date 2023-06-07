str = "123"
print(str)
print(str.replace("1", "www", 10))
print(str)

str = "The sum of 1 + 2 is {0}".format(1 + 2)
print(str)  # The sum of 1 + 2 is 3
str = "The sum of 1 + 2 is %s"
print(str % (1 + 2))  # The sum of 1 + 2 is 3
