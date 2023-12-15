
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
    # 14 / 23 
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key = lambda x: x[2])
        m = len(queries)
    
        #查找father
        father = list(range(n))
        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        #合并
        def join(u, v):
            fu = find(u)
            fv = find(v)
            if fu != fv:
                father[fu] = fv
        

        ans = [False] * m
        # qpair = sorted(enumerate(queries), key = lambda x: x[1][2])
        k = 0
        for i,q in sorted(enumerate(queries), key = lambda x: x[1][2]):
            while k < len(edgeList) and edgeList[k][2] < q[2]:
                join(edgeList[k][0],edgeList[k][1])
                k += 1
            ans[i] = find(q[0]) == find(q[1])
        return ans
    

    def distanceLimitedPathsExist2(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda e: e[2])

        # 并查集模板
        fa = list(range(n))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(from_: int, to: int) -> None:
            fa[find(from_)] = find(to)

        ans, k = [False] * len(queries), 0
        # 查询的下标按照 limit 从小到大排序，方便离线
        for i, (p, q, limit) in sorted(enumerate(queries), key=lambda p: p[1][2]):
            while k < len(edgeList) and edgeList[k][2] < limit:
                merge(edgeList[k][0], edgeList[k][1])
                k += 1
            ans[i] = find(p) == find(q)
        return ans

    

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]

sol = Solution()
print(sol.distanceLimitedPathsExist(n, edgeList, queries))
