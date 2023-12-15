
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
    def finalString2(self, s: str) -> str:    
        ans = []
        for v in s:
            if v != 'i':
                ans.append(v)
            else:
                next = []
                for i in range(len(ans) - 1, -1, -1):
                    next.append(ans[i])
                ans = next
        return ''.join(ans)
    
    def finalString(self, s: str) -> str:    
        ans = []
        for v in s:
            if v != 'i':
                ans.append(v)
            else:
                ans = ans[::-1]

        return ''.join(ans)
    
    
s = "string"
s = "poiinter"
# print(s[::-1])
sol = Solution()
print(sol.finalString(s))
