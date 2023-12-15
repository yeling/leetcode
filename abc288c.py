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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(n, m, edges):
    # g = [[] for _ in range(n + 1)]
    # for i,j in edges:
    #     g[i].append(j)
    #     g[j].append(i)
    #查找father
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
    father = list(range(n + 1))
    ans = 0
    for u,v in edges:
        if find(father,u) == find(father,v):
            ans += 1
        else:
            join(father,u,v)
    print(ans)


n,m = li()
edges = []
for i in range(0, m):
    edges.append(li())
main(n, m, edges)
