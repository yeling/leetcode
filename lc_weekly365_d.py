
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
    # 932 / 941 个 TLe
    def countVisitedNodes2(self, edges: List[int]) -> List[int]: 
        #基环树, 求环，入度为0的点，dfs到环的距离
        n = len(edges)
        vis = [False] * n
        ans = [0] * n
        #curr环上位置
        for i in edges:
            tempVis = [False] * n
            curr = edges[i]
            while tempVis[curr] == False:
                tempVis[curr] = True
                curr = edges[curr]
            #环上节点
            cache = list()
            while vis[curr] == False:
                cache.append(curr)
                vis[curr] = True
                curr = edges[curr]
            for v in cache:
                ans[v] = len(cache)

        ins = [[] for _ in range(n)]
        for i,v in enumerate(edges):
            ins[v].append(i)
        #
        leaf = []
        for i in range(n):
            if len(ins[i]) == 0:
                leaf.append(i)
        def dfs(curr):
            nonlocal vis
            nonlocal ans
            # print(curr)
            if vis[curr] == False:
                dfs(edges[curr])
                vis[curr] = True
                ans[curr] = ans[edges[curr]] + 1

        for v in leaf:
            dfs(v)
        # print(cache, ans, ins)
        return ans
    
    # 932 / 941 个 TLe
    # AC
    def countVisitedNodes(self, edges: List[int]) -> List[int]: 
        #基环树, 求环，入度为0的点，dfs到环的距离
        # vis数组分两层，一层给dfs使用，使用ans数组来表示节点是否被访问过
        n = len(edges)
        vis = [False] * n
        ans = [0] * n
        def dfs(curr):
            # nonlocal visd
            nonlocal ans
            # print(curr)
            if ans[curr] == 0:
                dfs(edges[curr])
                ans[curr] = ans[edges[curr]] + 1
            return
        
        for i in range(n):
            if vis[i] == True:
                continue
            curr = i
            while vis[curr] == False:
                vis[curr] = True
                curr = edges[curr]
            #环上节点
            if ans[curr] == 0:
                tempVis = [False] * n
                cache = list()
                while tempVis[curr] == False:
                    cache.append(curr)
                    tempVis[curr] = True
                    curr = edges[curr]
                for v in cache:
                    ans[v] = len(cache)
            # print(i, ans, vis)
            dfs(i)
        
        return ans
    
edges = [1,2,0,0,1]
# edges = [1,2,3,4,0]
edges = [6,3,6,1,0,8,0,6,6]
edges = [3,6,1,0,5,7,4,3]
edges = [18,18,4,6,1,8,14,4,16,11,13,6,10,10,6,18,14,11,4]
sol = Solution()
print(sol.countVisitedNodes(edges))
print(sol.countVisitedNodes2(edges))
