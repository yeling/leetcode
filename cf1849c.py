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
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve2(n, m, s, op):
    cache = set()
    for l,r in op:
        temp = [v for v in s]
        se = temp[l - 1:r]
        se.sort()
        b = temp[0:l - 1] + se + temp[r:]
        cache.add(tuple(b))
    print(len(cache))
    return 

def solve(n, m, str, op):
    cache = set()
    pre1 = [-1] * n
    after0 = [-1] * (n)
    #记录1->0
    preChange = [0] * n
    for i in range(1,n):
        if str[i - 1] == '1':
            pre1[i] = i - 1
        else:
            pre1[i] = pre1[i - 1]
    for i in range(n - 2, -1, -1):
        if str[i + 1] == '0':
            after0[i] = i + 1
        else:
            after0[i] = after0[i + 1]
    for i in range(1,n):
        preChange[i] = preChange[i - 1]
        if str[i - 1] == '1' and str[i] == '0':
            preChange[i] += 1

    ans = 0
    flag = False
    for l,r in op:
        l -= 1
        r -= 1
        s = pre1[l] + 1
        e = after0[r] - 1
        if preChange[r] - preChange[l] == 0:
            flag = True
        else:
            cache.add((s,e))
    ans = len(cache)
    if flag:
        ans += 1
        
    print(ans)
        
    return

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    str = input()
    op = []
    for _ in range(m):
        op.append(li())
    # solve2(n, m, str, op)
    solve(n, m, str, op)

   
