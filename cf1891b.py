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
input = sys.stdin.buffer.readline
input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def check(n, q, nums, qs):
    ans = nums[:]
    for i in range(q):
        for j in range(n):
            if ans[j]%(2 ** qs[i]) == 0:
                ans[j] += 2 ** (qs[i] - 1)
    print(*ans)

    return 

def solve2(n, q, nums, qs):
    ans = nums[:]
    for j in range(n):
        for i in range(q):
            if ans[j]%(2 ** qs[i]) == 0:
                ans[j] += 2 ** (qs[i] - 1)
            elif ans[j]%2 == 1:
                break
    
    print(*ans)


def solve(n, q, nums, qs):
    ans = nums[:]
    tq = [qs[0]]
    for i in range(1,q):
        if qs[i] < tq[-1]:
            tq.append(qs[i])
    # print(tq)
    for j in range(n):
        for i in range(len(tq)):
            if ans[j]%(2 ** tq[i]) == 0:
                ans[j] += 2 ** (tq[i] - 1)
            elif ans[j]%2 == 1:
                break
    
    print(*ans)
    return 
caseNum = int(input())
for i in range(0, caseNum):
    n,q = li()
    nums = li()
    qs = li()
    solve(n, q, nums, qs)

   
