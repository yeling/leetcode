
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue


MOD = 10 ** 9 + 7
class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost
 
    def __init__(self, V):
        self.G = [[] for i in range(V)]
        self._E = 0
        self._V = V
 
    @property
    def E(self):
        return self._E
 
    @property
    def V(self):
        return self._V
 
    def add_edge(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1
 
    def shortest_path(self, s):
        import heapq
        que = []
        d = [10**15] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))
 
        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost: continue
 
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    heapq.heappush(que, (d[e.to], e.to))
        return d
    
class Solution:
    def minScore2(self, n: int, roads: List[List[int]]) -> int:
        dis = [10**10]*(1 + n)
        dis[1] = 0
        vis = [False] * (1 + n)
        stack = PriorityQueue()
        #(index,w)
        g = [list() for _ in range(1 + n)]
        for v in roads:
            print(v)
            g[v[0]].append((v[1],v[2]))
            g[v[1]].append((v[0],v[2]))
        #(dis,index)
        stack.put((0,1))
        while not stack.empty():
            curr = stack.get()
            vis[curr[1]] = True
            for v in g[curr[1]]:
                if v[0] != curr[1] and vis[v[0]] == False:
                    dis[v[0]] = min(dis[v[0]], dis[curr[1]] + v[1])
                    stack.put((dis[v[0]], v[0]))
        
        return dis[n]

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def find(father, u):
            if father[u] != u:
                father[u] = find(father,father[u])
            return father[u]
        #合并
        def join(father, u, v):
            fu = find(father,u)
            fv = find(father,v)
            if fu != fv:
                father[fu] = fv
        father = [i for i in range(n+1)]
        for v in roads:
            join(father, v[0], v[1])
        
        g = [list() for _ in range(1 + n)]
        for v in roads:
            # print(v)
            g[v[0]].append((v[1],v[2]))
            g[v[1]].append((v[0],v[2]))
        
        dst = find(father, father[1])
        allRoad = []
        for i in range(n+1):
            fa = find(father, father[i])
            if fa == dst:
                for v in g[i]:
                    allRoad.append(v[1])
    
        return min(allRoad)
    
n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
sol = Solution()
print(sol.minScore(n, roads))
