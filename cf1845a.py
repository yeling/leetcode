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

def solve(n, k, x):
    if x != 1:
        print(YES)
        print(n)
        print(*[1]*n)
        return
    elif k == 2:
        if n%2 == 0:
            print(YES)
            ans = [2]*(n//2)
            print(len(ans))
            print(*ans)
        else:
            print(NO)
    elif k > 2:
        if n%2 == 0:
            print(YES)
            ans = [2]*(n//2)
            print(len(ans))
            print(*ans)
        else:
            ans = [2]*(n//2)
            ans[-1] = 3
            print(YES)
            print(len(ans))
            print(*ans)
    else:
        print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,x = lint()
    solve(n, k, x)

   
