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


def main(n, m, graph):
    #查找father
    def find(u):
        if father[u] != u:
            fu = find(father[u])
            father[u] = fu
        return father[u]
    
    #合并
    def join(u, v):
        fu = find(u)
        fv = find(v)
        if fu != fv:
            father[fu] = fv
            edges[fv] += edges[fu] + 1
            # edges[fu] = 0
        else:
            edges[fv] += 1

    father = list(range(n + 1))
    edges = [0] * (n + 1)
    
    for u,v in graph:
        join(u, v)

    rootMap = defaultdict(int)
    for i in range(1, n+1):
        fa = find(father[i])
        # if i != fa:
        #     edges[fa] += edges[i]
        rootMap[fa] += 1

    # print(father)
    # print(rootMap)
    # print(edges, len(edges))
    for k in rootMap:
        if k != 0:
            if rootMap[k] != edges[k]:
                print('No')
                return 
    print('Yes')
    

n,m = li()
nums = []
for i in range(0, m):
    nums.append(li())

main(n, m, nums)