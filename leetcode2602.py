
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
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        nums.sort()
        pre = [0]*(n + 1)
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        for v in queries:
            i = bisect_left(nums, v)
            temp = i*v - pre[i] + pre[n] - pre[i] - (n - 1 - i + 1) * v
            ans.append(temp)

        return ans
    
nums = [3,1,6,8]
queries = [1,5]
nums = [2,9,6,3]
queries = [10]
sol = Solution()
print(sol.minOperations(nums, queries))
