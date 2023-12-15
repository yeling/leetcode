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


# input = lambda: sys.stdin.readline().rstrip()
input = lambda: sys.stdin.readline().rstrip()
sint = lambda :int(input())
mint = lambda :map(int,input().split())
lint = lambda :list(mint())


def solve(n, k):
    ans = 0
    # print('in', n)
    while n > 0:
        ans += n%3
        n = n//3
        # print(n)
    # print(n, ans)
    if k >= ans and (k - ans)%2 == 0:
        print(YES)
    else:
        print(NO) 
    
    return

# n = 163
# k = 79
# solve(n, k)

caseNum = int(input())
for i in range(0, caseNum):
    n,k = lint()
    solve(n, k)

