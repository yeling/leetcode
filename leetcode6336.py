
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Graph:

    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, n: int, edges: List[List[int]]):
        self.G = [[] for i in range(n)]
        self._E = len(edges)
        self._V = n
        for u,v,c in edges:
            self.add_edge(u,v,c)
    
    def add_edge(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1


    def addEdge(self, edge: List[int]) -> None:
        u,v,c = edge
        self.add_edge(u,v,c)
        return 


    def shortestPath(self, node1: int, node2: int) -> int:
        import heapq
        que = []
        d = [10**15] * self._V
        d[node1] = 0
        heapq.heappush(que, (0, node1))

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    heapq.heappush(que, (d[e.to], e.to))
        # print(node1, node2, d, d[node2])
        if d[node2] == 10**15:
            return -1
        else:
            return d[node2]
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
    