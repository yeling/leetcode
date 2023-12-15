
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import time

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    #状态压缩DP + 折半搜素 + 双指针
    # 72 / 73
    def minAbsDifference3(self, nums: List[int], goal: int) -> int:
        pre = set()
        after = set()
        n = len(nums)
        half = n//2
        for i in range(0, 2 ** half):
            s = 0
            temp = i
            j = 0
            while temp > 0:
                if temp & 1 > 0:
                    s += nums[j]
                j += 1
                temp >>= 1
            pre.add(s)
        
        for i in range(1, 2 ** (n - half)):
            s = 0
            temp = i
            j = 0
            while temp > 0:
                if temp & 1 > 0:
                    s += nums[half + j]
                j += 1
                temp >>= 1
            after.add(s)
        pre = sorted(pre)
        after = sorted(after)
        # print(pre, after)
        ans = INF
        for v in pre:
            ans = min(ans, abs(v - goal))
        if ans == 0:
            return ans

        for v in after:
            ans = min(ans, abs(v - goal))
        if ans == 0:
            return ans
        # print(ans)
        i = 0
        j = len(after) - 1
        while i < len(pre) and j >= 0:
            temp = pre[i] + after[j]
            ans = min(ans, abs(temp - goal))
            if temp > goal:
                j -= 1
            elif temp == goal:
                ans = 0
                break
            else:
                i += 1
            # print(ans, i, j )
        return ans
    
    def minAbsDifference2(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def state_compress(lst):
            m = len(lst)
            bit = {1<<i: lst[i] for i in range(m)}
            dp=[0]*(1<<m)
            for i in range(1, 1<<m):
                dp[i]=dp[i^i&-i]+bit[i&-i]
            return sorted(list(set(dp)))

        pre = state_compress(nums[:n//2])
        post = state_compress(nums[n//2:])

        ans = abs(goal)
        i = 0
        j = len(post)-1
        while i < len(pre) and j >= 0:
            ans = min(ans, abs(goal-pre[i]-post[j]))
            if not ans:
                return ans
            if pre[i]+post[j] > goal:
                j -= 1
            elif pre[i]+post[j] < goal:
                i += 1
        return ans

    #状态压缩DP + 折半搜素 + 双指针
    # 72 / 73
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        pre = set()
        after = set()
        n = len(nums)
        half = n//2
        dp = [0] * (2 ** half)

        bit = {1<<i: nums[i] for i in range(n)}
        # print(bit)

        for i in range(1, 2 ** half):
            dp[i] = dp[i - (i&(-i))] +  bit[i&(-i)]
        pre = set(dp)
        
        dp = [0] * (2 ** (n - half))
        for i in range(1, 2 ** (n - half)):
            dp[i] = dp[i - (i&(-i))] +  bit[(i&(-i))<<half]
            
        after = set(dp)

        pre = sorted(pre)
        after = sorted(after)
        # print(pre, after)
        ans = INF
        for v in pre:
            ans = min(ans, abs(v - goal))
        if ans == 0:
            return ans

        for v in after:
            ans = min(ans, abs(v - goal))
        if ans == 0:
            return ans
        # print(ans)
        i = 0
        j = len(after) - 1
        while i < len(pre) and j >= 0:
            temp = pre[i] + after[j]
            ans = min(ans, abs(temp - goal))
            if temp > goal:
                j -= 1
            elif temp == goal:
                ans = 0
                break
            else:
                i += 1
            # print(ans, i, j )
        return ans
    
nums = [7,-9,15,-2]
goal = -5

# nums = [1,2,3]
# goal = -7

# nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,-8192,-16384,-32768,-65536,-131072,-262144,-524288]
# goal = 1048574
start = time.time()

sol = Solution()
print(sol.minAbsDifference2(nums, goal))
print(sol.minAbsDifference(nums, goal))

end = time.time()
print("used %.2f second "%(end-start))
