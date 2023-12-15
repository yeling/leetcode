
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
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d
        print(nums)
        nums.sort()
        ans = 0
        for i in range(1,n):
            ans += (nums[i] - nums[i-1]) * i * (n - i) %MOD
        return ans%MOD
    

nums = [-2,0,2]
s = "RLL"
d = 3
nums = [1,0]
s = "RL"
d = 2
sol = Solution()
print(sol.sumDistance(nums, s, d))
