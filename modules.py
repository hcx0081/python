import os
import time

sec = time.time()
print(sec)

print(time.localtime(sec))

import urllib.request

print(urllib.request.urlopen("http://www.baidu.com").read())

os.system("calc.exe")
