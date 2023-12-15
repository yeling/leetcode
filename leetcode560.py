
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        s = 0
        ans = 0
        for i,v in enumerate(nums):
            s += v
            if s == k:
                ans += 1
            ans += cache[s - k]
            cache[s] += 1
        return ans
    
nums = [1,2,3]
k = 3
nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))
