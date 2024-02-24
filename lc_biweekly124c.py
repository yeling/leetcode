
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

# 456 / 549 个通过测试用例
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)
        @cache
        def dfs(i, j , dst):
            if i == j:
                return 0
            
            curr = 0
            if i + 1 <= j and nums[i] + nums[i + 1] == dst:
                curr = max(curr, 1 + dfs(i + 2, j, dst))
            if j > i and nums[i] + nums[j] == dst:
                curr = max(curr, 1 + dfs(i + 1, j - 1, dst))
            if j - 1 >= i and nums[j] + nums[j - 1] == dst:
                curr = max(curr, 1 + dfs(i, j - 2, dst))
            return curr

        t = 1 + dfs(2, n - 1, nums[0] + nums[1])
        ans = max(t, ans)
        t = 1 + dfs(1, n - 2, nums[0] + nums[-1])
        ans = max(t, ans)
        t = 1 + dfs(0, n - 3, nums[-2] + nums[-1])
        ans = max(t, ans)
        return ans
    
nums = [3,2,1,2,3,4]
nums = [3,2,6,1,4]
nums = [1,1,1,1,1,1]
sol = Solution()
print(sol.maxOperations(nums))
