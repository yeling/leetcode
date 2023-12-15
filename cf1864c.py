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
    ans = []
    ma = len(bin(n)[2:])
    ans = [1<<i for i in range(ma)]
    # print(bin(n)[2:], ans)
    for i in range(ma-2,-1,-1):
        if (1 << i) & n != 0:
            ans.append(ans[-1] + (1<<i))
    print(len(ans))
    print(*ans[::-1])



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    solve(n)

   
