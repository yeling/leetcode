
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7

class Solution:
    # TLE 39 / 45 个通过测试用例
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                temp = nums[i:j+1]
                temp.sort()
                m = len(temp)
                # print(m, temp)
                if m%2 == 0 and k == temp[(m - 1)//2]:
                    count += 1
                elif m%2 == 1 and k == temp[m//2]:
                    count += 1
                    
        return count

    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        dp = [0] * n
        dst = -1
        pre = defaultdict(int)
        after = defaultdict(int)
        for i,v in enumerate(nums):
            if v > k:
                dp[i] = dp[i-1] + 1
            elif v == k:
                dst = i
                dp[i] = dp[i-1]
            elif v < k:
                dp[i] = dp[i-1] -1
            if dst == -1:
                pre[dp[i]] += 1
            elif i >= dst:
                after[dp[i]] += 1
        
        count = 0
        # print(dp, pre, after)
        for i in range(dst + 1):
            if i == 0:
                count += after[0] + after[1]
            else:
                count += after[dp[i-1]] + after[dp[i-1] + 1]
        
        return count
    
nums = [3,2,1,4,5]
k = 4
nums = [7,8,3,2,1,5,4,6]
k = 3
# nums = [2,3,1]
# k = 3

sol = Solution()
print(sol.countSubarrays2(nums,k))
print(sol.countSubarrays(nums,k))
