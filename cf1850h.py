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

def solve(n, m, nums):
    inList = [[] for i in range(n + 1)]
    outList = [[] for i in range(n + 1)]
    pos = [-1] * (n + 1)
    for a,b,d in nums:
        if d >= 0:
            outList[a].append((b,d))
            inList[b].append((a,d))
        else:
            inList[a].append((b,-d))
            outList[b].append((a,-d))

    stack = []
    for i in range(1,n + 1):
        if len(inList[i]) == 0:
            stack.append(i)
            pos[i] = 1
        
    if len(stack) == 0:
        print(NO)
        return
    
    while len(stack) > 0:
        next = []
        for v in stack:
            for k in outList[v]:
                if pos[k[0]] == -1 or pos[k[0]] == pos[v] + k[1]:
                    pos[k[0]] = pos[v] + k[1]
                    next.append(k[0])
                else:
                    print(NO)
                    return
        stack = next
        # print(pos)
    print(YES)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = []
    for _ in range(m):
        nums.append(li())
    solve(n, m, nums)


   
