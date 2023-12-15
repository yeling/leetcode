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


def main(n, m, nums):
    father = list(range(n))
    for v in nums:
        join(father, v[0] - 1, v[1] - 1)

    rootMap = defaultdict(int)
    for i in range(len(father)):
        fa = find(father, father[i])
        rootMap[fa] += 1

    print(len(rootMap))
    

n,m = li()
nums = []
for i in range(m):
    nums.append(li())
main(n, m, nums)
   
