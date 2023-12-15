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
MOD = 998244353

mi = lambda :map(int,input().split())
li = lambda :list(mi())


#TLE
def main2(q, qs):
    s = "1"
    l = 0
    for v in qs:
        if v[0] == 1:
            s += str(v[1])
        elif v[0] == 2:
            l += 1
        elif v[0] == 3:
            temp = int(s[l:])
            print(temp%MOD)
    

def main(q, qs):
    s = "1"
    l = 0
    for v in qs:
        if v[0] == 1:
            s += str(v[1])
        elif v[0] == 2:
            l += 1
        elif v[0] == 3:
            temp = int(s[l:])
            print(temp%MOD)
    


q = int(input())
qs = []
for _ in range(q):
    qs.append(li())
main(q, qs)
