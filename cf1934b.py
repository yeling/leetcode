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
    cache = [0,1,2,1,2,3,1,2,3,2,1,2,2,2,3,1]
    ans = n//15 + cache[n%15]
    if n%15 == 5 and n//15 >= 1:
        ans -= 2
    if n%15 == 8 and n//15 >= 1:
        ans -= 1
    # print("f " , n, ans)
    for i in range(1,16):
        ans = min(ans, n//i * cache[i] + cache[n%i])
        # print(i, ans)
    print(ans)
    return 

def check(n):
    ans = n
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    for e in range(n):
                        if a + 3*b + 6*c + 10 * d + 15*e == n:
                            ans = min(ans, a + b + c + d + e)
    print(n, ans)
    return

# for i in range(30):
#     check(i)
#     solve(i)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)

   
