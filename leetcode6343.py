
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
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
    # 1028 / 1040 个通过测试用例
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:   
        dij = Dijkstra(2*len(specialRoads) + 2)
        allV = [(start[0], start[1],0)]
        index = 1
        for v in specialRoads:
            dij.add_edge(index, index + 1, v[4])
            # dij.add_edge(index + 1, index, v[4])
            allV.append((v[0],v[1],index))
            index += 1
            allV.append((v[2],v[3], index))
            index += 1
            

        allV.append((target[0], target[1],index))
        index += 1
        # print(allV)
        for i in range(len(allV)):
            for j in range(i+1, len(allV)):
                dij.add_edge(allV[i][2], allV[j][2], abs(allV[i][0] - allV[j][0]) + abs(allV[i][1] - allV[j][1]))
                dij.add_edge(allV[j][2], allV[i][2], abs(allV[i][0] - allV[j][0]) + abs(allV[i][1] - allV[j][1]))
        
        s = dij.shortest_path(0)
        # print(s)
        return s[-1]
    
    
start = [3,2]
target = [5,7]
specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]

# start = [1,1]
# target = [4,5]
# specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]

start = [1,1]
target = [10,4]
specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]

start = [1,1]
target = [10,8]
specialRoads = [[6,4,9,7,1],[5,2,2,1,3],[3,2,5,5,2]]

sol = Solution()
print(sol.minimumCost(start, target, specialRoads))
