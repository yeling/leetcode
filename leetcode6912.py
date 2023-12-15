
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
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = [1] * n
        dp2 = [1] * n
        ans = 1
        for i in range(1,n):
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = max(dp1[i], dp1[i - 1] + 1)
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = max(dp2[i], dp2[i - 1] + 1)
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
            ans = max(ans,dp1[i], dp2[i])
            # print(dp1, dp2)

        return ans
    
nums1 = [2,3,1]
nums2 = [1,2,1]
nums1 = [1,3,2,1]
nums2 = [2,2,3,4]
nums1 = [1]
nums2 = [2]
sol = Solution()
print(sol.maxNonDecreasingLength(nums1, nums2))
