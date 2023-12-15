
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
    def maxSum(self, nums: List[int], k: int) -> int:    
        cnt = [0] * 32
        for v in nums:
            for i in range(0,32):
                if (1 << i) & v != 0:
                    cnt[i] += 1
        # print(cnt)
        ans = 0
        for i in range(k):
            curr = 0
            for i in range(31, -1, -1):
                if cnt[i] > 0:
                    curr |= (1 << i)
                    cnt[i] -= 1
            ans += curr * curr
            ans %= MOD
        return ans%MOD
    
nums = [2,6,5,8]
k = 2
nums = [4,5,4,7]
k = 3
sol = Solution()
print(sol.maxSum(nums, k))
