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

def solve(n, m, k, a, b):
    i = 0
    j = 0
    cnta = [0] * (k + 1)
    for v in a:
        if v > k:
            continue
        cnta[v] = 1
    ac = sum(cnta)
    cntb = [0] * (k + 1)
    cnts = [0] * (k + 1)
    for v in b:
        if v > k:
            continue
        cntb[v] = 1
        if cnta[v] == 1:
            cnts[v] = 1
    bc = sum(cntb)
    sc = sum(cnts)

    if ac + bc - sc == k and (ac - sc <= k//2 and bc - sc <= k//2):
        print(YES)
    else:
        print(NO)



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,k = li()
    a = li()
    b = li()
    solve(n, m, k, a, b)

   
