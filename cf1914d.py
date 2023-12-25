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

def solve(n, a, b, c):
    all = [(a[i], b[i], c[i], i) for i in range(n)]
    pp = [0,1,2]
    ans = 0
    for p in permutations(pp):
        flag = [False] * n
        temp = 0
        for v in p:
            all.sort(key = lambda x: -x[v])
            for i in range(n):
                if flag[all[i][3]] == False:
                    temp += all[i][v]
                    flag[all[i][3]] = True
                    break
        ans = max(ans, temp)

    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    c = li()
    solve(n, a, b, c)

   
