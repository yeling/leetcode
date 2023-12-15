
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
    def maxKelements(self, nums: List[int], k: int) -> int:
        stack = PriorityQueue()
        for v in nums:
            stack.put(-v)
        ans = 0
        for _ in range(k):
            curr = -stack.get()
            ans += curr
            stack.put(ceil(-curr//3))
        return ans
    
nums = [1,10,3,3,3]
k = 3
nums = [10,10,10,10,10]
k = 5
sol = Solution()
print(sol.maxKelements(nums,k))
