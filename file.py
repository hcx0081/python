with open("D:/hello.txt") as file:
    print(file.closed)  # False
print(file.closed)  # True

try:
    file = open("D:/hello.txt")
    print(file.closed)  # False
finally:
    file.close()
print(file.closed)  # False
