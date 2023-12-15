
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
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ans = 0
        last = -1
        n = len(nums)
        for i,v in enumerate(nums):
            if v == 1:
                if last == -1:
                    last = i
                    ans = 1
                else:
                    ans *= i - last
                    ans %= MOD
                    last = i
        
        return ans%MOD
    
nums = [0,1,0,0,1,0,0]
nums = [0,1,0,0,0]
sol = Solution()
print(sol.numberOfGoodSubarraySplits(nums))
