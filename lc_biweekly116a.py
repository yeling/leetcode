
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
    def sumCounts(self, nums: List[int]) -> int:  
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                temp = set(nums[i:j+1])
                # print(temp)
                ans += len(temp) * len(temp)

        return ans
    
nums = [1,2,1]
nums = [2,2]
sol = Solution()
print(sol.sumCounts(nums))
