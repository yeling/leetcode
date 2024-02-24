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

def solve2(k, x, a):
    # print(k)
    if a - x <= 0:
        print(NO)
        return
    if (x + 1)%k == 0:
        print(YES)
    else:
        print(NO)
    
    
    return 

def solve(k, x, a):
    sum = 0
    k -= 1
    for _ in range(x + 1):
        bet = sum//k + 1
        sum += bet
        # print(bet, sum)
        if sum > a:
            break
        
    if sum <= a:
        print(YES)
    else:
        print(NO)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    k,x,a = li()
    solve(k, x, a)

   
