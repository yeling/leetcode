
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
    def minimumSum(self, n: int, k: int) -> int:
        ans = []
        cache = set()
        i = 1
        while len(ans) < n:
            if k - i not in cache:
                ans.append(i)
                cache.add(i)
            i += 1
        return sum(ans)
    
n = 5
k = 4
n = 2
k = 6
sol = Solution()
print(sol.minimumSum(n, k))
