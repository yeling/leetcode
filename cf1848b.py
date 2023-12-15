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

def solve(n, k, nums):
    cache = [[0, n + 1] for _ in range(k+1)]
    for i,v in enumerate(nums):
        cache[v].append(i + 1)
    # print(cache)
    ans = INF
    for i in range(1,k+1):
        cache[i].sort()
        diff = [(cache[i][j] - cache[i][j-1] - 1) for j in range(1,len(cache[i]))]
        ma = max(diff)
        diff.append((ma - 1)//2)
        diff.append(ma//2)
        diff.sort(reverse=True)
        ans = min(ans, diff[1])
    print(ans)



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    solve(n, k, nums)


   
