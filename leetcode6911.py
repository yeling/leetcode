
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
    def continuousSubarrays2(self, nums: List[int]) -> int: 
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                mi = INF
                ma = 0
                flag = True
                for k in range(i,j+1):
                    mi = min(mi, nums[k])
                    ma = max(ma, nums[k])
                    if nums[k] + 2 < ma or nums[k] - 2 > mi:
                        flag = False
                        break
                if flag:
                    ans += 1 
        return ans
    
    def continuousSubarrays(self, nums: List[int]) -> int: 
        n = len(nums)
        ans = 0
        l = 0
        r = 0
        cache = defaultdict(int)
        while r < n:
            cache[nums[r]] += 1
            #
            mi = min(cache.keys())
            ma = max(cache.keys())
            while ma - mi > 2:
                cache[nums[l]] -= 1
                if cache[nums[l]] == 0:
                    del cache[nums[l]]
                l += 1
                mi = min(cache.keys())
                ma = max(cache.keys())
            ans += r - l + 1
            # print( l, r , ans)
            r += 1

        return ans
    
nums = [5,4,2,4]
nums = [1,2,3]
nums = [2,3,1,5,4,2]

sol = Solution()
print(sol.continuousSubarrays2(nums))
print(sol.continuousSubarrays(nums))
