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

def solve(x, y, n):
    delta = 1
    curr = y
    ans = []
    for _ in range(n):
        ans.append(curr)
        curr = curr - delta
        delta += 1
    # print(ans, curr)
    if ans[-1] >= x:
        ans[-1] = x
        print(*ans[::-1])
    else:
        print(-1)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    x,y,n = li()
    solve(x, y, n)

   
