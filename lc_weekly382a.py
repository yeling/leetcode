
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(1,n):
            if s[i] == s[i - 1] or abs(ord(s[i]) - ord(s[i - 1])) == 32:
                continue
            else:
                ans += 1


        return ans
    
s = "Aaa"
sol = Solution()
print(sol.countKeyChanges(s))
