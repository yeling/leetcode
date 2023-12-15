
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ans = 0
        for i in range(k):
            ans += m
            m += 1

        return ans
    

nums = [1,2,3,4,5]
k = 3
nums = [5,5,5]
k = 2
sol = Solution()
print(sol.maximizeSum(nums, k))
