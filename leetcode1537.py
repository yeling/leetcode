
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    # 81 / 82 
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp1 = [0] * n
        dp2 = [0] * m
        m1 = [-1]*n

        j = 0
        for i in range(n):
            while j < m - 1 and nums2[j] < nums1[i]:
                j += 1
            if nums1[i] == nums2[j]:
                m1[i] = j
            i += 1
        # print(m1, m2)
        i = 0
        j = 0
        while i < n or j < m:
            if i < n and j < m:
                dp1[i] = max(dp1[i], dp1[i-1] + nums1[i])
                if m1[i] != -1:
                    while j <= m1[i]:
                        dp2[j] = max(dp2[j], dp2[j-1] + nums2[j])
                        j += 1
                    dp1[i] = max(dp1[i], dp2[m1[i]])
                    dp2[m1[i]] = max(dp1[i], dp2[m1[i]])
                i += 1
            elif i < n:
                dp1[i] = max(dp1[i], dp1[i-1] + nums1[i])
                i += 1
            elif j < m:
                dp2[j] = max(dp2[j], dp2[j-1] + nums2[j])
                j += 1
            # print(dp1, dp2, i, j)

        return max(dp1[n-1], dp2[m-1])%MOD


nums1 = [2, 4, 5, 8, 10]
nums2 = [4, 6, 8, 9]
nums1 = [1,3,5,7,9]
nums2 = [3,5,100]
nums1 = [1,4,5,8,9,11,19]
nums2 = [2,3,4,11,12]
nums1 = [10,12,19,26,31,34,36]
nums2 = [3,7,10,14,17,21]
# 61
sol = Solution()
print(sol.maxSum(nums1, nums2))
