
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
    #dp[i][j] 数值i,diff为j的最大长度
    #1.先计算之前到nums[i]的
    #2.新增长度为1的
    def longestArithSeqLength2(self, nums: List[int]) -> int:
        n = len(nums)
        ma = max(nums)
        #dp[i][diff]
        ans = 0
        dp = [defaultdict(int) for _ in range(ma + 1)]
        
        for i in range(-ma, ma + 1):
            dp[nums[0]][i] = 1
        # print(dp[nums[0]])
        for i in range(1,n):
            #先计算之前到nums[i]的
            for j in range(ma + 1):
                diff = nums[i] - j
                dp[nums[i]][diff] = max(dp[nums[i]][diff],dp[j][diff] + 1)
                ans = max(ans, dp[nums[i]][diff])
            #新增长度为1的
            for k in range(-ma, ma + 1):
                dp[nums[i]][k] = max(dp[nums[i]][k], 1)

            # print(nums[i],dp[nums[i]], dp[nums[i]][3])
    
        return ans
    
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ma = max(nums)
        #dp[i][diff]
        ans = 0
        dp = [[0]*(2*ma + 1)  for _ in range(ma + 1)]
        for i in range(-ma, ma + 1):
            dp[nums[0]][i + ma] = 1
        # print(dp[nums[0]])
        for i in range(1,n):
            #先计算之前到nums[i]的
            for j in range(ma + 1):
                diff = nums[i] - j + ma
                dp[nums[i]][diff] = max(dp[nums[i]][diff],dp[j][diff] + 1)
                ans = max(ans, dp[nums[i]][diff])
            #新增长度为1的
            for k in range(nums[i] - ma, ma + 1):
                dp[nums[i]][k] = max(dp[nums[i]][k], 1)

            # print(nums[i],dp[nums[i]], dp[nums[i]][3])
    
        return ans


# nums = [3,6,9,12]
# nums = [20,1,15,3,10,5,8]
nums = [9,4,7,2,10]
# nums = [61,28,67,53,13,6,70,5,79,82,60,60,84,17,80,25,82,82,69,76,81,43,58,86,18,78,4,25,8,30,33,87,91,18,90,26,62,11,28,66,9,33,58,66,47,48,80,38,25,57,4,84,79,71,54,84,63,32,97,62,26,68,5,69,54,93,25,26,100,73,24,94,80,39,30,45,95,80,0,29,57,98,92,15,17,76,69,11,57,56,48,10,28,7,63,66,53,58,12,58]
sol = Solution()
print(sol.longestArithSeqLength(nums))
