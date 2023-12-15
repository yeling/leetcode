
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
    def minOperations(self, nums: List[int], k: int) -> int:
        cache = set()
        n = len(nums)
        for i in range(n):
            cache.add(nums[-1-i])
            flag = True
            for j in range(1,k + 1):
                if j not in cache:
                    flag = False
                    break
            if flag:
                return i + 1

        return -1
    
nums = [3,1,5,4,2]
k = 2
nums = [3,2,5,3,1]
k = 3
sol = Solution()
print(sol.minOperations(nums, k))
