
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
    #暴力 2 ^ n
    def largestSumOfAverages1(self, nums: List[int], k: int) -> float:
        n = len(nums)
        lis = list(range(1,n))
        maxAve = 0
        for v in permutations(lis,k-1):
            temp = list(v)
            temp.sort()
            print(temp)
        #     temp = [1,4]
            ave = 0
            for i, v in enumerate(temp):
                if i == 0:
                    s = sum(nums[0:temp[0]])
                    ave += s/temp[0]
                else:
                    s = sum(nums[temp[i-1]:temp[i]])
                    ave += s/(temp[i] - temp[i-1])
            s = sum(nums[temp[len(temp) - 1]:])
            ave += s / (n - temp[len(temp) - 1])
            maxAve = max(maxAve, ave)
        return maxAve
    
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        #动态规划，写好转移方程
        n = len(nums)
        #前i个，划分为j个子数组
        dp  = [[0] * (k + 1) for _ in range(n)]
        # < i 的 sum
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
        
        for j in range(1,k+1):
            for i in range(j - 1, n):
                if j == 1:
                    dp[i][1] = preSum[i + 1]/(i + 1)
                else:
                    for si in range(0,i):
                        dp[i][j] = max(dp[i][j], dp[si][j-1] + (preSum[i + 1] - preSum[si + 1])/(i - si))
            # print(j , dp)
        return dp[n-1][k]

nums = [9,1,2,3,9]
k = 3
nums = [7,8,1,2,3,8,1,2]
k = 4
sol = Solution()
print(sol.largestSumOfAverages1(nums,k))
print(sol.largestSumOfAverages(nums,k))
