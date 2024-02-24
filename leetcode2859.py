
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
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,v in enumerate(nums):
            if bin(i).count('1') == k:
                ans += v
            # print(ans, v)
        return ans
    
nums = [5,10,1,5,2]
k = 1
sol = Solution()
print(sol.sumIndicesWithKSetBits(nums, k))
