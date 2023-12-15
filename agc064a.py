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
    # print(n)
    cnt = n * (n + 1)//2
    ans = [0] * cnt
    cache = list(range(0,n+1))
    cache.append(0)
    # print(cache)
    ans[0] = n - 1
    cache[n] -= 1
    cache[n - 1] -= 1
    ans[-1] = n
    r = cnt - 2
    
    l = 1
    while l <= r:
        if cache[ans[l - 1] + 1] > 0:
            ans[l] = ans[l - 1] + 1
            cache[ans[l - 1] + 1] -= 1
        elif cache[ans[l - 1] - 1] > 0:
            ans[l] = ans[l - 1] - 1
            cache[ans[l - 1] - 1] -= 1
        elif cache[ans[l - 1] - 2] > 0:
            ans[l] = ans[l - 1] - 2
            cache[ans[l - 1] - 2] -= 1

        if cache[ans[r + 1] + 1] > 0:
            ans[r] = ans[r + 1] + 1
            cache[ans[r + 1] + 1] -= 1
        elif cache[ans[r + 1] - 1] > 0:
            ans[r] = ans[r + 1] - 1
            cache[ans[r + 1] - 1] -= 1
        elif cache[ans[r + 1] - 2] > 0:
            ans[r] = ans[r + 1] - 2
            cache[ans[r + 1] - 2] -= 1
        r -= 1
        l += 1
        # print(ans, cache)
    
    print(*ans)
    
    return

# solve(6)

n = int(input())
solve(n)

