
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 1963 / 2003 个通过测试用例

    def longestString(self, x: int, y: int, z: int) -> int:   
        if x != y: 
            ans = 2*min(x,y) + 1 + z 
        else:
            ans = 2*x + z
        return 2*ans
    
x = 2
y = 5
z = 1
x = 3
y = 2
z = 2
x = 9
y = 9
z = 34
sol = Solution()
print(sol.longestString(x, y, z))
