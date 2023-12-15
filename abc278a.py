# auther yeling
from typing import List
from collections import *

n, k  = [int(v) for v in (input()).split(' ')]
nums = [int(v) for v in (input()).split(' ')]

# print(n , k)
res = deque(nums)
for i in range(k):
    res.popleft()
    res.append(0)
resStr = ''
for v in res:
    resStr += str(v) + ' '
print(resStr)
