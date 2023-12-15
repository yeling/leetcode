
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
    # 581 / 590 
    def specialPerm(self, nums: List[int]) -> int:
        #1.壮压DP 待选集合i，上一次的选择j，然后进行下一次选择
        n = len(nums)
        
        @cache
        def dfs(i, j):
            #集合被用完了，说明找到了一组
            # print(i, j)
            if i == 0:
                return 1
            #遍历i中元素，和 j的关系
            ans = 0
            for k in range(n):
                if i >> k & 1 > 0 and (nums[k]%nums[j] == 0 or nums[j]%nums[k] == 0):
                    ans += dfs(i ^ (1 << k), k)
            return ans
        return sum([dfs(((1<<n) - 1) ^ (1 << k), k ) for k in range(n)])%MOD
    
    
nums = [2,3,6]
nums = [1,4,3]
sol = Solution()
print(sol.specialPerm(nums))
