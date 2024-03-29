
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
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int: 
        ans = 0
        cache = set()
        for v in arr1:
            t = v
            while t > 0:
                cache.add(str(t))
                t //= 10   
        for v in arr2:
            t = v
            while t > 0:
                if str(t) in cache:
                    ans = max(ans, len(str(t)))
                t //= 10
        return ans
    
arr1 = [1,10,100]
arr2 = [1000]
arr1 = [1,2,3]
arr2 = [4,4,4]
sol = Solution()
print(sol.longestCommonPrefix(arr1, arr2))

