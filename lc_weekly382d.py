
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
    # 548 / 822 
    def minOrAfterOperations2(self, nums: List[int], k: int) -> int:
        cache = [0] * 30
        for v in nums:
            print(bin(v)[2:])
            for i in range(30):
                if ((1 << i) & v) > 0:
                    cache[i] += 1
            # print(cache)
        ans = 0
        print(cache)
        for i,v in enumerate(cache):
            if v > k:
                ans |= (1 << i)
        return ans
    
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        cache = defaultdict(set)
        for i,v in enumerate(nums):
            for j in range(30):
                if ((1 << j) & v) > 0:
                    cache[j].add(i)
        print(cache)
        ans = 0
        curr = set()
        for i in range(29,-1,-1):
            if len(cache[i]) > k:
                ans |= (1 << i)
            else:
                temp = curr
                for v in cache[i]:
                    temp.add(v)
                if len(temp) <= k:
                    curr = temp
                else:
                    ans |= (1 << i)
            print(i, ans)
        return ans
    
nums = [3,5,3,2,7]
k = 2
nums = [7,3,15,14,2,8]
k = 4
nums = [10,7,10,3,9,14,9,4]
k = 1

#34 38
nums = [39,62,35,11,28,32]
k = 3
sol = Solution()
print(sol.minOrAfterOperations2(nums, k))
print(sol.minOrAfterOperations(nums, k))
