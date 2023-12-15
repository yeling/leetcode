
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
    def removeTrailingZeros(self, num: str) -> str:    
        if num == '0':
            return num
        i = 0
        n = len(num)
        while i < len(num) and num[-1-i] == '0':
            i += 1
        ans = num[0:n-i]
        return ans
    
num = "10"
sol = Solution()
print(sol.removeTrailingZeros(num))
