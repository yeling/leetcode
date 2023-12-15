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

def solve(n, k, q, qs):
    #[value,index]
    stack = []
    cache = []
    for i in range(n):
        temp = [0,i]
        cache.append(temp)
        heappush(stack, temp)

    for x,y in qs:
        # print(x,y, stack)
        ans = 0
        cache[x-1][0] = -y
        top = []
        temp = heappop(stack)
        heappush(stack, temp)

        for i in range(k):
            temp = heappop(stack)
            ans += -temp[0]
            top.append(temp)
        
        for v in top:
            heappush(stack, v)
        print(ans)
        # print(ans)
    return

n,k,q = li()
qs = []
for _ in range(q):
    qs.append(li())

solve(n, k, q, qs)

