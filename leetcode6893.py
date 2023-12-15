
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
    # 271 / 587 个通过测试用例
    # 529 / 587 个通过测试用例 MLE
    def specialPerm2(self, nums: List[int]) -> int:   
        n = len(nums)
        dp = [[False] * n for _ in range(n)]
        self.ans = 0
        for i in range(n):
            for j in range(n):
                if nums[i]%nums[j] == 0:
                    dp[i][j] = True
                    dp[j][i] = True

        @cache
        def dfs(index, vis, cnt, path):
            # print(index, vis, cnt, path)
            vis = list(vis)
            path = list(path)
            if cnt == n:
                self.ans = (self.ans + 1)%MOD
                return
            for i in range(n):
                if vis[i] == False and dp[index][i] == True:
                    vis[i] = True
                    path.append(nums[i])
                    dfs(i, tuple(vis), cnt + 1, tuple(path))
                    vis[i] = False
                    path.pop()


            return
        
        vis = [False]*n
        for i in range(n):
            vis[i] = True
            path = tuple([nums[i]])
            dfs(i, tuple(vis), 1, path)
            vis[i] = False
        
        return self.ans
    
    def specialPerm(self, nums: List[int]) -> int:   
        n = len(nums)
        dp = [[False] * n for _ in range(n)]
        self.ans = 0
        for i in range(n):
            for j in range(n):
                if nums[i]%nums[j] == 0:
                    dp[i][j] = True
                    dp[j][i] = True

        @cache
        def dfs(index, vis, cnt, path):
            # print(index, vis, cnt, path)
            vis = list(vis)
            path = list(path)
            if cnt == n:
                print(path)
                self.ans = (self.ans + 1)%MOD
                return
            for i in range(n):
                if vis[i] == False and dp[index][i] == True:
                    vis[i] = True
                    path.append(nums[i])
                    dfs(i, tuple(vis), cnt + 1, tuple(path))
                    vis[i] = False
                    path.pop()


            return
        
        vis = [False]*n
        for i in range(n):
            vis[i] = True
            path = tuple([nums[i]])
            dfs(i, tuple(vis), 1, path)
            vis[i] = False
        
        return self.ans
    
nums = [2,3,6]
nums = [1,4,3]
nums = [20,100,50,5,10,70,7]
sol = Solution()
print(sol.specialPerm(nums))
