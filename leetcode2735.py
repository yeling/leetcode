
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 936 / 2564 个通过测试用例
    # 1021 / 2564 个通过测试用例
    # 1031 / 2564 个通过测试用例

    def minCost2(self, nums: List[int], x: int) -> int:
        cnt = 0
        minPos = -1
        mi = INF
        n = len(nums)
        for i,v in enumerate(nums):
            if mi > v:
                mi = v
                minPos = i
        cnt += nums[minPos]
        curr = minPos
        currVal = mi
        for _ in range(n-1):
            next = curr + 1 if curr < n - 1 else 0
            if currVal + x < nums[next]:
                cnt += currVal + x
            else:
                cnt += nums[next]
                currVal = nums[next]
            curr = next
        return cnt
    
    def minCost3(self, nums: List[int], x: int) -> int:
        cnt = 0
        minPos = -1
        mi = INF
        n = len(nums)
        for i,v in enumerate(nums):
            if mi > v:
                mi = v
                minPos = i
        cnt += nums[minPos]
        curr = minPos
        currVal = mi
        for _ in range(n-1):
            next = curr + 1 if curr < n - 1 else 0
            if currVal + x < nums[next]:
                cnt += currVal + x
            else:
                cnt += nums[next]
                currVal = nums[next]
            curr = next
        return cnt
    
    # 1031 / 2564 个通过测试用例
    # AC
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [[INF]*n for _ in range(n)]
        for i in range(n):
            temp = nums[i]
            for j in range(i,n+i):
                temp = min(temp, nums[j%n])
                dp[i][j%n] = temp
        # print(dp)
        ans = sum(nums)
        for i in range(1,n):
            temp = i * x
            for j in range(n):
                temp += dp[(j - i + n)%n][j]
            ans = min(ans, temp)
            
        return ans
    
    
nums = [20,1,15]
x = 5
# nums = [8,2,5,3,1]
# x = 3

# nums = [31,25,18,59]
# x = 27

#298
# nums = [15,150,56,69,214,203]
# x = 42
sol = Solution()
print(sol.minCost(nums, x))
