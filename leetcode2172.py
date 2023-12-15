
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
    #TLE
    def maximumANDSum2(self, nums: List[int], numSlots: int) -> int:
        #数位DP
        # i 表示还没有放的数字集合， j 表示当前slot的集合 ，两个为一组
        # 从 i 中取出一个数字，放入j中
        n = len(nums)
        self.cnt = 0
        @cache
        def dfs(i,j):
            self.cnt += 1
            print(i, j, self.cnt)
            if i == 0:
                return 0
            ans = 0
            for ik in range(n):
                if i >> ik & 1 == 0:
                    continue
                for jk in range(2*numSlots):
                    if j >> jk & 1 == 1:
                        continue
                    ans = max(ans, (nums[ik] & (jk//2 + 1)) + dfs(i ^(1 << ik), j | (1 << jk)))
            return ans        
        return dfs((1 << n) - 1, 0)
    
    #TLE
    # 4 / 84
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        #数位DP
        # i 表示已经放的数字集合， j 表示当前slot的集合 ，两个为一组
        # 从 i 中取出一个数字，放入j中
        n = len(nums)
        self.cnt = 0
        @cache
        def dfs(i,slot):
            self.cnt += 1
            # print(i, slot, self.cnt)
            if i == (1 << n) - 1:
                return 0
            ans = 0
            for ik in range(n):
                if i >> ik & 1 == 1:
                    continue
                for jk in range(numSlots):
                    if slot[jk] == 2:
                        continue
                    next = list(slot)
                    next[jk] += 1
                    if nums[ik] & (jk + 1) > 0:
                        ans = max(ans, (nums[ik] & (jk + 1)) + dfs(i |(1 << ik), tuple(next)))
            return ans        
        return dfs(0, tuple([0]*numSlots))
    
nums = [1,2,3,4,5,6]
numSlots = 3

nums = [1,3,10,4,7,1]
numSlots = 9

nums = [14,7,9,8,2,4,11,1,9]
numSlots = 8

sol = Solution()
# print(sol.maximumANDSum(nums, numSlots))
print(sol.maximumANDSum(nums, numSlots))
