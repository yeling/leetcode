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
    ans = 0
    for v in b:
        ans += a[v-1]

    print(ans)


n, m = li()
a = li()
b = li()
main(n, m, a, b)

