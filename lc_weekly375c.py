
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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = max(nums)
        pos = []
        for i,v in enumerate(nums):
            if v == m:
                pos.append(i)
        # print(pos)
        ans = 0
        np = len(pos)
        for i,v in enumerate(pos):
            if i + k - 1 < len(pos):
                if i == 0:
                    ans += (pos[i] + 1) * (n - pos[i + k - 1])
                else:
                    ans += (pos[i] - pos[i - 1]) * (n - pos[i + k - 1])                
        return ans
    
nums = [1,3,2,3,3]
k = 2
# nums = [1,4,2,1]
# k = 3
sol = Solution()
print(sol.countSubarrays(nums, k))
