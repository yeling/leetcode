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
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve2(n, s, t):
    diffA = 0
    diffB = 0
    for i in range(n):
        if s[i] != t[i]:
            diffA += 1
        if s[i] != t[-1-i]:
            diffB += 1
    ans = 0
    if diffA < diffB:
        ans = diffA
        if diffA == 0:
            ans = 0
        elif diffA%2 == 1:
            ans = 2 * diffA - 1
        elif diffA%2 == 0:
            ans = 2 * diffA 
    else:
        ans = diffB
        if diffB == 0:
            ans = 2
        elif diffB%2 == 1:
            ans = 2 * diffB
        else:
            ans = 2 * diffB - 1
        
    print(ans)
    
    return 

def solve(n, s, t):
    diffA = 0
    diffB = 0
    for i in range(n):
        if s[i] != t[i]:
            diffA += 1
        if s[i] != t[-1-i]:
            diffB += 1
    
    ansA = diffA
    if diffA == 0:
        ansA = 0
    elif diffA%2 == 1:
        ansA = 2 * diffA - 1
    elif diffA%2 == 0:
        ansA = 2 * diffA 
    
    ansB = diffB
    if diffB == 0:
        ansB = 2
    elif diffB%2 == 1:
        ansB = 2 * diffB
    else:
        ansB = 2 * diffB - 1
        
    print(min(ansA, ansB))
    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    t = input()
    # solve2(n, s, t)
    solve(n, s, t)

   
