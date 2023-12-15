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


def main(n, t, c, r):
    tmax = -1
    tpos = -1
    oneMax = r[0]
    onePos = 0
    for i in range(n):
        if c[i] == t:
            if r[i] > tmax:
                tmax = r[i]
                tpos = i
        if c[i] == c[0]:
            if r[i] > oneMax:
                oneMax = r[i]
                onePos = i

    if tpos != -1:
        print(tpos + 1)
    else:
        print(onePos + 1)
        



n,t = li()
c = li()
r = li()
main(n, t, c, r)