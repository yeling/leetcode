
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
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[-INF]*(m + 1) for _ in range(n + 1)]
        dp[1][1] = nums1[0] * nums2[0]
        for i in range(n):
            for j in range(m):
                # if nums1[i] * nums2[j] > 0:
                #     dp[i + 1][j + 1] = dp[i][j] + nums1[i] * nums2[j]
                # else:
                dp[i + 1][j + 1] = max(nums1[i] * nums2[j], dp[i][j] + nums1[i] * nums2[j], dp[i + 1][j + 1], dp[i+1][j], dp[i][j+1])
        return dp[n][m]
    
nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
# nums1 = [3,-2]
# nums2 = [2,-6,7]
# nums1 = [-8,-1]
# nums2 = [1,1]

sol = Solution()
print(sol.maxDotProduct(nums1, nums2))
