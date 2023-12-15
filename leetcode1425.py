
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
    # 20 / 36 TLE
    def constrainedSubsetSum2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [v for v in nums]
        ans = -INF
        # print(dp)
        for i in range(n):
            ans = max(ans, dp[i])
            if dp[i] <= 0:
                continue
            for j in range(1, k+1):
                if i + j < n:
                    dp[i + j] = max(dp[i + j], dp[i] + nums[i+j])
            # print(i, dp)
        return ans
    
    # 20 / 36 TLE
    # 30 / 36
    # 31 / 36 TLE
    #1.记录下一个正数的位置，如果可以直接跳跃
    #2.
    def constrainedSubsetSum3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        #下一个大于0的数所在的位置
        next = [-1] * n
        pos = -1
        for i in range(n-1, -1, -1):
            next[i] = pos
            if nums[i] >= 0:
                pos = i
        # print(next)

        dp = [v for v in nums]
        ans = -INF
        # print(dp)
        i = 0
        while i < n:
            ans = max(ans, dp[i])
            if dp[i] <= 0:
                i += 1
                continue
            if nums[i] >= 0 and next[i] != -1 and next[i] - i <= k: 
                dp[next[i]] = max(dp[next[i]], dp[i] + nums[next[i]])
                i = next[i]
            else:
                for j in range(1, k+1):
                    if i + j < n:
                        dp[i + j] = max(dp[i + j], dp[i] + nums[i+j])
                i += 1
            
            # print(i, dp)
        return ans
    
    
    def constrainedSubsetSum4(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [v for v in nums]
        ans = -INF
        # print(dp)
        for i in range(n):
            start = max(0, i - k)
            for j in range(start, i):
                ans = max(ans, dp[i])
                dp[i] = max(dp[i], dp[j] + nums[i])            
            print(i, dp)
        return ans

    # 1.动态规划+单调队列
    # dp[j]动态递减，大于对尾的出队列
    # 队头坐标大于K的也出掉
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [v for v in nums]
        ans = dp[0]
        # print(dp)
        #(dp[j],j)
        stack = deque()
        for i in range(n):
            #1.从0的位置，计算当前值，0的位置是最大值
            #2.当前位置入队列，小于当前值的出队列
            #3.从队头去除位置大于k的
            if len(stack) > 0:
                dp[i] = stack[0][0] + nums[i]
            ans = max(ans, dp[i])
            #2.当前位置入队列，小于当前值的出队列
            if dp[i] > 0:
                while len(stack) > 0:
                    tail = stack[-1]
                    if tail[0] < dp[i]:
                        stack.pop()
                    else:
                        break
                stack.append((dp[i],i))
            # 3.从队头去除位置大于k的
            while len(stack) > 0:
                if i - stack[0][1] >= k:
                    stack.popleft()
                else:
                    break     
            # print(i, dp, stack)
        return ans

    
nums = [10,2,-10,5,20]
k = 2
nums = [10,-2,-10,-5,20]
k = 2
nums = [-2,-1,-3]
k = 1

# nums = [10,10,10,10,-10,-1,-10,-1,-10,10,10,10,10]
# nums = [40,-10,-1,-10,-1,-10,40]
# k = 3

sol = Solution()
print(sol.constrainedSubsetSum2(nums,k))
print(sol.constrainedSubsetSum(nums,k))
