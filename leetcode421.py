
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:    
        n = len(nums)
        nums.sort()
        ans = 0
        for v in nums:
            print(bin(v)[2:])

        print(nums, nums[0] ^ nums[-1])
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, nums[i]^nums[j])
                # print(bin(nums[i]), bin(nums[j]))
        return ans
    
# nums = [3,10,5,25,2,8]
nums = [14,70,53,83,49,91,36,80,92,51,66,70]
sol = Solution()
print(sol.findMaximumXOR(nums))
