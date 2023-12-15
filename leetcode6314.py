
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
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        father = [-1] * n
        #bfs 求出father
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        stack = []
        stack.append(0)
        vis = [False] * n
        vis[0] = True
        # print(graph)
        while len(stack) > 0:
            size = len(stack)
            for i in range(size):
                curr = stack[i]
                vis[curr] = True
                for v in graph[curr]:
                    if i != v and vis[v] == False:
                        father[v] = curr
                        stack.append(v)
            stack = stack[size:]
            # print(stack)
        cache = set()
        for f,c in guesses:
            cache.add((f,c))
        print(cache)
        print(father)
        ans = 0
        currk = 0
        for i in range(n):
            if father[i] == -1:
                currk = 0
                for i in range(1,n):
                    if (i,father[i]) in cache:
                        currk += 1
                    if currk >= k:
                        ans += 1
                        break
            else:
                #father变换
                temp = father[i]
                father[i] = -1
                while father[temp] != -1:
                    pre = father[temp]
                    father[temp] = temp
                    temp = pre
                father[temp] = temp




        return
    
edges = [[0,1],[1,2],[2,3],[3,4]]
guesses = [[1,0],[3,4],[2,1],[3,2]]
k = 1
edges = [[0,1],[1,2],[1,3],[4,2]]
guesses = [[1,3],[0,1],[1,0],[2,4]]
k = 3

sol = Solution()
print(sol.rootCount(edges, guesses, k))
