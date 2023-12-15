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

def solve(n, nums):
    cache = defaultdict(list)
    for i,v in enumerate(nums):
        cache[v].append(i)
    
    cnt = 0
    for k in cache:
        if len(cache[k]) >= 2:
            cnt += 1
    if cnt == 1 or cnt == 0:
        print(-1)
        return
    ans = [1] * n
    curr = True
    # print(cache)
    for k in cache:
        if len(cache[k]) >= 2:
            for v in cache[k]:
                if curr:
                    ans[v] = 2
                else:
                    ans[v] = 3
            ans[cache[k][0]] = 1
            curr = not curr
    print(*ans)



    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)


   
