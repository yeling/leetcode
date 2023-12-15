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

def solve(n, x, k):
    # print(n)
    # 向下
    ans = 0
    mi = x << k
    ma = x << k
    for i in range(k):
        ma |= (1 << i)
    if n >= ma:
        ans += ma - mi + 1
    elif mi <= n < ma:
        ans += n - mi + 1
    elif n < mi:
        ans = 0
    #向上
    up = ans
    if k > 1:
        ans += pow(2 , k - 1)
    print(up, ans)

    

    return

caseNum = int(input())
for i in range(0, caseNum):
    n,x,k = li()
    solve(n, x, k)

