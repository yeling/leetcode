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

def solve(n):
    s = int(sqrt(10 ** (n - 1)))
    e = int(sqrt(10 ** (n))) + 1
    all = []
    for i in range(s,e):
        all.append(i*i)
    
    print(len(all), s, e)
    return 

def check():
    ans = []
    for i in range(100):
        ans.append((i,i*i))
    print(*ans)
    return

for i in range(1, 16):
    solve(i)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)
   
