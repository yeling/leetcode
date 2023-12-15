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


def main(n, t, a):
    # print(n,t,a)
    s = sum(a)
    t = t % s
    ts = 0
    for i,v in enumerate(a):
        ts += v
        if ts > t:
            print(i + 1, v - (ts - t))
            break


n,t = mi()
a = li()    
main(n,t,a)

