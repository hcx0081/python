a = {'one': 1, 'two': 2, 'three': 3}

b = dict(one=1, two=2, three=3)

c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

d = dict({'one': 1, 'three': 3}, two=2)
e = dict([('two', 2), ('one', 1), ('three', 3)])
f = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e == f)  # True
