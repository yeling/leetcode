
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
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cache = set(nums)
        n = len(nums)
        ans = 0
        for i in range(n):
            temp = set()
            for j in range(i,n):
                temp.add(nums[j])
                if len(temp) == len(cache):
                    ans += 1

        return ans
    
nums = [1,3,1,2,2]
nums = [5,5,5,5]
sol = Solution()
print(sol.countCompleteSubarrays(nums))
