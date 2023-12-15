
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
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for v in nums:
            cnt[v%value] += 1
        m = INF
        pos = -1
        for i,v in enumerate(cnt):
            if v < m:
                m = v
                pos = i
        ans = m * value + pos
        return ans
    
nums = [1,-10,7,13,6,8]
value = 5
nums = [1,-10,7,13,6,8]
value = 7
sol = Solution()
print(sol.findSmallestInteger(nums, value))
