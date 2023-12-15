
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
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        ans = 0
        for v in nums:
            if cache[k - v] != 0:
                ans += 1
                cache[k - v] -= 1
            else:
                cache[v] += 1

        return ans
    
nums = [3,1,3,4,3]
k = 6
nums = [1,2,3,4]
k = 5
sol = Solution()
print(sol.maxOperations(nums,k))
