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

def solve2(n, p, l, t):
    ma = (n - 1)//7 + 1
    study = 0
    s = 0
    left = ma
    while s < p:
        if left > 0:
            curr = min(left, 2)
            left -= 2
            s += t * curr
        s += l
        study += 1
    print(n - study)
    return 

def solve(n, p, l, t):
    ma = (n - 1)//7 + 1
    study = 0
    if (ma // 2) * ( 2 * t + l) >= p:
        study = (p + (2 * t + l - 1))//(2 * t + l)
    else:
        study = ma // 2
        study += 1 + max(0,(p - (ma//2) * ( 2 * t + l) - ma%2 * t - l + l - 1)//l) 
    
    print(n - study)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,p,l,t = li()
    # solve2(n, p, l, t)
    solve(n, p, l, t)

   
