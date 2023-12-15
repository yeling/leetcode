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

def solve2(x, y):
    # print(x, y)
    ans = 0
    if len(x) != len(y):
        y = y[0:len(y) - len(x)]
        ans = len(x) * 9
        for i in range(len(y)):
            ans += int(y[i])
        print(ans)
    else:
        ans = 0
        for i in range(len(x)):
            ans += abs(int(x[i]) - int(y[i]))
            if ans > 0:
                ans += (len(x) - i - 1) * 9
                break
        print(ans)
    return 

def solve(x, y):
    # print(x, y)
    ans = 0
    if len(x) != len(y):
        ans = int(y[0]) + 9 * (len(y) - 1)
        print(ans)
    else:
        ans = 0
        for i in range(len(x)):
            ans += abs(int(x[i]) - int(y[i]))
            if ans > 0:
                ans += (len(x) - i - 1) * 9
                break
        print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    x, y = input().split()
    solve(x, y)

   
