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


def main(n, q, qs):
    box = [list() for _ in range(n + 1)]
    numCache = defaultdict(set)
    for v in qs:
        if v[0] == 1:
            box[v[2]].append(v[1])
            numCache[v[1]].add(v[2])
        elif v[0] == 2:
            box[v[1]].sort()
            print(*box[v[1]])
        elif v[0] == 3:
            temp = list(numCache[v[1]])
            temp.sort()
            print(*temp)
    
n = int(input())
q = int(input())
qs = []
for _ in range(q):
    qs.append(li())
main(n, q, qs)
