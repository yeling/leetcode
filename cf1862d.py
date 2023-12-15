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
    # print(int(sqrt(2*n)))
    k = int(sqrt(2*n)) + 1
    while k * (k - 1) > 2 * n:
        k -= 1
    ans = k + n - k * (k - 1)//2
    print(ans)
    return 

def solve2(n) -> None:
    k = int(sqrt(n * 2))
    if k * (k + 1) == n * 2:
        print(k + 1)
    else:
        while k * (k + 1) > n * 2:
            k -= 1
        # print("k",k)
        print(k + 1 + n - k * (k + 1) // 2)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)
    # solve2(n)

   
