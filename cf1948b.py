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

def solve(n, nums):
    curr = 0
    for v in nums:
        temp = deque()
        t = v
        if t == 0:
            temp.append(0)
        while t > 0:
            temp.appendleft(t%10)
            t //= 10
        t1 = list(temp)
        t2 = list(temp)
        t2.sort()
        if curr <= t2[0] and t1 == t2:
            curr = t2[-1] 
        elif curr <= v:
            curr = v
        else:
            print(NO)
            return
    print(YES)

        # print(temp, t2)


    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)

   
