
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
    def findScore(self, nums: List[int]) -> int:
        stack = PriorityQueue()
        for i,v in enumerate(nums):
            stack.put((v,i))
        ans = 0
        n = len(nums)
        vis = [False]*(n + 1)
        while stack.empty() == False:
            temp = stack.get()
            if vis[temp[1]] == False:
                ans += temp[0]
                vis[temp[1]] = True
                if temp[1] != 0:
                    vis[temp[1] - 1] = True
                if temp[1] != n - 1:
                    vis[temp[1] + 1] = True
                # print("ans = ", temp[0], ans, vis)

            # print(temp)
        return ans
    
nums = [2,1,3,4,5,2]
nums = [2,3,5,1,3,2]
sol = Solution()
print(sol.findScore(nums))
