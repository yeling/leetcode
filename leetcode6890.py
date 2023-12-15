
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = INF
        for i in range(1,n):
            ans = min(ans, nums[i] - nums[i-1])
        
        return ans
    
nums = [1,3,2,4]
nums = [100,1,10]
sol = Solution()
print(sol.findValueOfPartition(nums))
