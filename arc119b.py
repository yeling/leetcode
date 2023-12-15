# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

#记录0的下标，从s中移动到t，或者从t移动到s
#位置不同就移动一次
#
def main(n, s, t):
    s = [int(v) for v in s]
    t = [int(v) for v in t]
    p, q = [], []
    for i, v in enumerate(s):
        if v == 0:
            p.append(i)
    
    for i, v in enumerate(t):
        if v == 0:
            q.append(i)
    if len(p) != len(q):
        print(-1)
        return
    res = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            res += 1
    print(res)
    
            
n = int(input())
s = input()
t = input()
main(n, s, t)
