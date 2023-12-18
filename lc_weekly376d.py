
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
    # 664 / 774 个通过测试用例
    # 673 / 774 个通过测试用例
    def maxFrequencyScore2(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        pre = [0] * (n + 1)
        ans = 0
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        for i in range(n):
            for j in range(i,n):
                v1 = (pre[j + 1] - pre[i])//(j - i + 1)
                temp = [v1 - 1, v1, v1 + 1]
                for v in temp:
                    p = bisect_left(nums, v)
                    if p < n:
                        cnt = (p - i) * v - (pre[p] - pre[i]) + pre[j + 1] - pre[p] - (j + 1 - p) * v
                        if cnt <= k:
                            ans = max(ans, j - i + 1)
                    # print(i, j , temp, ans)

        return ans
    
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        pre = [0] * (n + 1)
        ans = 0
        for i,v in enumerate(nums):
            pre[i + 1] = pre[i] + v
        for i in range(n):
            for j in range(i,n):
                v1 = (pre[j + 1] - pre[i])//(j - i + 1)
                temp = [v1 - 1, v1, v1 + 1]
                for v in temp:
                    p = bisect_left(nums, v)
                    if p < n:
                        cnt = (p - i) * v - (pre[p] - pre[i]) + pre[j + 1] - pre[p] - (j + 1 - p) * v
                        if cnt <= k:
                            ans = max(ans, j - i + 1)
                    # print(i, j , temp, ans)

        return ans
    
nums = [1,2,6,4]
k = 3
# nums = [1,4,4,2,4]
# k = 0
# nums = [28,6,22,10]
# k = 12
nums = [24,6,14,6,30,9,6,11,21,10,12,27,1]
k = 90
sol = Solution()
print(sol.maxFrequencyScore(nums, k))
