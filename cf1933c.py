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

def solve(a, b, l):
    ans = 0
    cache = set()
    for x in range(0,30):
        if (a ** x) > l:
            continue
        for y in range(0,30):
            t = (a ** x) * (b ** y)
            if t <= l and l%t == 0:
                cache.add(l//t)
            if t > l:
                break
    print(len(cache))
    return

caseNum = int(input())
for i in range(0, caseNum):
    a,b,l = li()
    solve(a, b, l)
    

   
