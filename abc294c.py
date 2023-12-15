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


def main(n, m, a, b):
    ai = []
    bi = []
    pa = 0
    pb = 0
    curr = 1
    while pa < n or pb < m:
        if pa < n:
            if pb == m:
                pa += 1
                ai.append(curr)
                curr += 1
            else:
                if a[pa] < b[pb]:
                    pa += 1
                    ai.append(curr)
                    curr += 1
                else:
                    pb += 1
                    bi.append(curr)
                    curr += 1
        elif pa == n:
            pb += 1
            bi.append(curr)
            curr += 1
    print(*ai)
    print(*bi)




n,m = li()
a = li()
b = li()
main(n, m, a, b)

