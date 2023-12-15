
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
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        base = [i for i in range(1,n)]
        base.append(n - 1)
        # print(base)
        for i in range(n):
            if base[i] == nums[i]:
                continue
            else:
                return False
        return True
        
    
nums = [3, 4, 4, 1, 2, 1]
sol = Solution()
print(sol.isGood(nums))
