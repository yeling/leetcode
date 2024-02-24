
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
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        cache = defaultdict(list)
        for i,v in enumerate(nums):
            cache[v].append(i)
        for k in cache:
            temp = n - 1 - cache[k][-1] + cache[k][0]
            for j in range(1,len(cache[k])):
                temp = max(temp, cache[k][j] - cache[k][j - 1] - 1)
            ans = min(ans, (temp + 1)//2)
              
        return ans
    
nums = [2,1,3,3,2]
nums = [1,2,1,2]
nums = [5,5,5,5]
sol = Solution()
print(sol.minimumSeconds(nums))
