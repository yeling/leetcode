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

input = lambda: sys.stdin.readline().rstrip()
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, q, s, qs):
    s = [v for v in s]
    print(s)
    #diff为偶数，两个连续
    l = 0 
    r = 0
    for v in s:
        if v == '(':
            l += 1
        elif v == ')':
            r += 1
    for v in qs:
        if s[v - 1] == '(':
            s[v- 1] = ')'
            l -= 1
            r += 1
        else:
            s[v - 1] = '('
            l += 1
            r -= 1
        if s[0] != '(' or s[-1] != ')':
            print(NO)
        elif (l - r)%2 == 0:
            print(YES)
        else:
            print(NO)
    return 


n,q = li()
s = input()
qs = []
for _ in range(q):
    qs.append(int(input()))
solve(n, q, s, qs)


   
