
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
from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:  
        n = len(nums)
        pre = [0] * (n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        sl = SortedList()
        ans = 0
        sl.add(0)
        for i,v in enumerate(nums):
            lp = sl.bisect_right(pre[i + 1] - lower)
            up = sl.bisect_left(pre[i + 1] - upper)
            ans += lp - up
            sl.add(pre[i + 1])
            # print(up, lp, ans)
            
          
        return ans
    
nums = [-2,5,-1]
lower = -2
upper = 2
nums = [0]
lower = 0
upper = 0
sol = Solution()
print(sol.countRangeSum(nums, lower, upper))
