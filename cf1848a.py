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

def solve(n, m, k, begin, fpos):
    # print(n, m, k)
    even = 0
    a, b = begin

    for x,y in fpos:
        if (abs(a - x) + abs(b - y))%2 == 0:
            even += 1
    if even >= 1:
        print(NO)
    else:
        print(YES)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m,k = li()
    begin = li()
    fpos = []
    for _ in range(k):
        fpos.append(li())
    solve(n, m, k, begin, fpos)



   
