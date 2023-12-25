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

def solve(s):
    if s.count('0') == s.count('1'):
        print(0)
        return
    n = len(s)
    ans = 0
    pre = [[0,0] for _ in range(n + 1)]
    for i,v in enumerate(s):
        pre[i + 1] = pre[i][:]
        if v == '0':
            pre[i + 1][0] += 1
        elif v == '1':
            pre[i + 1][1] += 1

    for i,v in enumerate(s):
        if v == '0':
            if pre[i + 1][0] > pre[n][1]:
                ans = n - i
                break
        elif v == '1':
            if pre[i + 1][1] > pre[n][0]:
                ans = n - i
                break

    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
