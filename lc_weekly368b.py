
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
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = INF
        pre = [INF] * (n + 1)
        sufix = [INF] * (n + 1)
        for i in range(n):
            pre[i + 1] = min(pre[i], nums[i])
            sufix[n - 1 - i] = min(sufix[n - i], nums[n - 1 - i])
        # print(pre, sufix)

        for i in range(1, n - 1):
            if pre[i] < nums[i] and nums[i] > sufix[i + 1]:
                ans = min(ans, pre[i] + nums[i] + sufix[i + 1])
            # print(nums[i], ans)
        if ans == INF:
            ans = -1


        return ans

nums = [8,6,1,5,3]  
nums = [6,5,4,3,4,5]
# nums = [5,4,8,7,10,2]

sol = Solution()
print(sol.minimumSum(nums))
