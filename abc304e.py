# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

# mi = lambda: map(int, sys.stdin.buffer.readline().split())
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

def solve(n, m, points, ks, qs ):
    father = list(range(1+n))
    for u,v in points:
        join(father, u, v)
    
    kf = set()
    begin = True
    for u,v in ks:
        fu = find(father, u)
        fv = find(father, v)
        if fu == fv:
            begin = False
            break
        kf.add((fu,fv))
    if begin == False:
        for _ in range(len(qs)):
            print(NO)

    for u, v in qs:
        fu = find(father, u)
        fv = find(father, v)
        if (fu,fv) in kf or (fv, fu) in kf:
            print(NO)
        else:
            print(YES)
    
    return


n, m = li()
points = []
for _ in range(m):
    points.append(li())
k = int(input())
ks = []
for _ in range(k):
    ks.append(li())

q = int(input())
qs = []
for _ in range(q):
    qs.append(li())

solve(n, m, points, ks, qs )




