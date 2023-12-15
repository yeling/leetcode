
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
    def minOperations(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = 0
        for v in nums:
            if curr >= v:
                ans += curr - v
                curr += 1
            else:
                curr = v + 1
            # print(v, curr, ans)
        return ans

nums = [1,1,1]
# nums = [1,5,2,4,1]
sol = Solution()
print(sol.minOperations(nums))
