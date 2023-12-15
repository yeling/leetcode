
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
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        allRes = set()
        n = len(nums)
        def dfs(i: int, pre: List[int]):
            if i == n:
                if len(pre) >= 2:
                    allRes.add(tuple(pre))
                return 
            #do nothing
            dfs(i + 1, pre)
            #select
            if len(pre) == 0 or nums[i] >= pre[-1]:
                pre.append(nums[i])
                dfs(i+1, pre)
                pre.pop()
            return
        
        dfs(0,[])
        # print(allRes)
        return list(map(list,allRes))
    
nums = [4,4,3,2,1]
nums = [4,6,7,7]
sol = Solution()
print(sol.findSubsequences(nums))
