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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve2(n, q, nums):
    g = [set() for _ in range(n+1)]
    for v in nums:
        if v[0] == 1:
            g[v[1]].add(v[2])
            g[v[2]].add(v[1])
        elif v[0] == 2:
            for iv in g[v[1]]:
                g[iv].remove(v[1])
            g[v[1]].clear()
        ans = 0
        for i in range(1,n+1):
            if len(g[i]) == 0:
                ans += 1
        print(ans)


    # print(n)

def solve(n, q, nums):
    g = [set() for _ in range(n+1)]
    ans = set(range(1,n+1))
    for v in nums:
        if v[0] == 1:
            g[v[1]].add(v[2])
            g[v[2]].add(v[1])
            if v[1] in ans:
                ans.remove(v[1])
            if v[2] in ans:
                ans.remove(v[2])
        elif v[0] == 2:
            for iv in g[v[1]]:
                g[iv].remove(v[1])
                if len(g[iv]) == 0:
                    ans.add(iv)
            g[v[1]].clear()
            ans.add(v[1])
        
        print(len(ans))



n,q = li()
nums = []
for _ in range(q):
    nums.append(li())
solve(n, q, nums)

