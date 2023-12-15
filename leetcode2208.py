
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
    def halveArray(self, nums: List[int]) -> int:   
        stack = []
        s = 0
        for v in nums:
            s += v
            heappush(stack, -v)
        dst = s/2
        ans = 0
        while dst > 0:
            temp = heappop(stack)
            dst += temp/2
            heappush(stack, temp/2)
            ans += 1

        return ans
    
nums = [5,19,8,1]
nums = [1]
sol = Solution()
print(sol.halveArray(nums))
