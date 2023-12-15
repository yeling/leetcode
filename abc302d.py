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


def solve(n, m, d, a, b):
    ans = -1
    # a.sort()
    b.sort()
    for v in a:
        dst = v + d
        pos = bisect_left(b, dst)
        if pos == m:
            pos = m - 1
        if abs(b[pos] - v) <= d:
            ans = max(ans, v + b[pos])
        if abs(b[pos - 1] - v) <= d:
            ans = max(ans, v + b[pos - 1])
        # print(v, pos)

    print(ans)
    return 


n,m,d = li()
a = li()
b = li()
solve(n, m, d, a, b)

