
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
    def maxSubarrayLength2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                temp = defaultdict(int)
                for id in range(i, j + 1):
                    temp[nums[id]] += 1
                flag = True
                for v in temp:
                    if temp[v] == k:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ans = max(ans, j - i + 1)
                # print(temp)
        return ans
    # 316 / 992 个通过测试用例

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        r = 0
        curr = defaultdict(int)
        while r < n:
            while r < n and curr[nums[r]] < k:
                # print(r, need, curr)
                curr[nums[r]] += 1
                if curr[nums[r]] > k:
                    break
                ans = max(ans, r - l + 1)
                r += 1
            if r < n:
                curr[nums[r]] += 1
                while l < n and curr[nums[r]] > k:
                    curr[nums[l]] -= 1
                    l += 1  
                r += 1      
        return ans
    
nums = [1,2,3,1,2,3,1,2]
k = 2
# nums = [1,2,1,2,1,2,1,2]
# k = 1
# nums = [5,5,5,5,5,5,5]
# k = 4
nums = [2]
k = 2
sol = Solution()
print(sol.maxSubarrayLength(nums, k))
