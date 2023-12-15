
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
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        n = len(forts)
        for i in range(n):
            if forts[i] == -1:
                l = i - 1
                while l >= 0 and forts[l] == 0:
                    l -= 1
                if l >= 0 and forts[l] == 1:
                    ans = max(ans, i - 1 - l)
                r = i + 1
                while r < n and forts[r] == 0:
                    r += 1
                if r < n and forts[r] == 1:
                    ans = max(ans, r - (i + 1))
        return ans
 
forts = [1,0,0,-1,0,0,0,0,1]
# forts = [0,0,1,-1]

sol = Solution()
print(sol.captureForts(forts))
