
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
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(0,n,2):
            ans.append(nums[i + 1])  
            ans.append(nums[i])
        return ans
    
nums = [5,4,2,3]
sol = Solution()
print(sol.numberGame(nums))
