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


def main(n, m, nums):
    vis = [False] * (n + 1)
    next = [0] * (n + 1)
    ans = []
    for v in nums:
        next[v] = v + 1
    for i in range(1, n + 1):
        if vis[i] == False:
            temp = []
            temp.append(i)
            vis[i] = True
            cur = i
            while next[cur] != 0:
                temp.append(next[cur])
                vis[next[cur]] = True
                cur = next[cur]
            temp.sort(reverse=True)
            for v in temp:
                ans.append(v)
    print(*ans)


n,m = li()
nums = li()
main(n, m, nums)
