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
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())

def solve(s, m, l, r):
    #每次找最远的一位
    cache = [int(v) for v in s]
    
    pos = [[] for _ in range(10)]
    for i,v in enumerate(cache):
        pos[v].append(i)
    # print(pos)
    curr = -1
    next = -1
    for i in range(m):
        for j in range(int(l[i]), int(r[i]) + 1):
            temp = bisect(pos[j], curr)
            if temp == len(pos[j]):
                print(YES)
                return
            next = max(next, pos[j][temp])
        curr = next
    print(NO)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    m = sint()
    l = input()
    r = input()
    solve(s, m, l, r)

   
