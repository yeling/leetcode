
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
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cache = []
        n = len(s)
        for i in range(n):
            for j in range(i,n):
                temp = s[i:j+1]
                if temp.count('1') == k:
                    cache.append(s[i:j+1])
        cache.sort(key=lambda x: (len(x), x))
        # print(cache)
        return cache[0] if len(cache) > 0 else ""
    
s = "100011001"
k = 3
s = "000"
k = 1
sol = Solution()
print(sol.shortestBeautifulSubstring(s, k))
