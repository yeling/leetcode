
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
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 16 / 131 个通过的测试用例
    def minimumFuelCost2(self, roads: List[List[int]], seats: int) -> int:
        g = defaultdict(list)
        for u,v in roads:
            g[u].append(v)
            g[v].append(u)
        #
        ret = 0
        def dfs(root, father):
            # 1,2,3,4
            nonlocal ret
            ans = [0] * (seats + 1)
            for v in g[root]:
                if v != father:
                    curr = dfs(v, root)
                    for i in range(1, seats + 1):
                        ans[i] += curr[i]
                        if curr[i] != 0:
                            ret += 1
            flag = False
            for i in range(seats - 1, 0, -1):
                if ans[i] != 0:
                    flag = True
                    ans[i] -= 1
                    ans[i + 1] += 1
                    break
            if flag == False:
                ans[1] += 1
            # print(root, ans, ret)
            return ans
        
        ans = dfs(0, -1)
        # print(ans)
        return ret
    
    # 16 / 131 个通过的测试用例
    # 可以换车
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = defaultdict(list)
        for u,v in roads:
            g[u].append(v)
            g[v].append(u)
        #
        ret = 0
        def dfs(root, father):
            # 1,2,3,4
            nonlocal ret
            ans = 1
            for v in g[root]:
                if v != father:
                    curr = dfs(v, root)
                    ans += curr
                    ret += (curr + seats - 1)//seats
            
            # print(root, ans, ret)
            return ans
        
        ans = dfs(0, -1)
        # print(ans)
        return ret
    
roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
seats = 2
roads = [[0,1],[0,2],[1,3],[1,4]]
seats = 2

sol = Solution()
print(sol.minimumFuelCost(roads, seats))
