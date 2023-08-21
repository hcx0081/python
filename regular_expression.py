import re

str = "   aaa   aaa   "
print(re.sub("\s+", "", str))
print(str)
