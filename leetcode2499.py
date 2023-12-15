
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # AC
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        cache = [0]*(n+1)
        s = 0
        for i in range(n):
            if nums1[i] == nums2[i]:
                cache[nums1[i]] += 1
                s += i

        ma = 0
        maxValue = -1
        for i,v in enumerate(cache):
            if v > ma:
                ma = v
                maxValue = i
        ans = 0
        total = sum(cache)
        maCnt = nums1.count(maxValue) + nums2.count(maxValue)
        if maCnt > n:
            return -1
        
        if ma > total//2:
            ans = ma
            ans = 0
            extra = ma - (total - ma)
            for i in range(n):
                if nums1[i] == nums2[i]:
                    ans += i
                elif extra > 0 and nums1[i] != maxValue and nums2[i] != maxValue:
                    ans += i
                    extra -= 1
        else:
            ans = (total + 1)//2
            ans = 0
            for i in range(n):
                if nums1[i] == nums2[i]:
                    ans += i
            

        return ans
    
nums1 = [3,2,2,1,3]
nums2 = [1,2,2,2,3]

# nums1 = [1,2,2]
# nums2 = [1,2,2]
nums1 = [1,1,1]
nums2 = [1,1,1]

sol = Solution()
print(sol.minimumTotalCost(nums1, nums2))
