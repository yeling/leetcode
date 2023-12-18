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

def solve(n, s):
    big = [s[-1]]
    flag = [True] * n
    flag[-1] = False
    for i in range(n-2, -1, -1):
        if s[i] >= big[-1]:
            big.append(s[i])
            flag[i] = False
    j = 0
    if flag[0] == True:
        pre = s[0]
    else:
        pre = big[0]
        j = 1

    for i in range(1,n):
        if flag[i] == True: 
            if s[i] >= pre:
                pre = s[i]
                continue
            else:
                print(-1)
                return  
        else:
            if big[j] >= pre:
                pre = big[j]
                j += 1
            else:
                print(-1)
                return
    print(len(big)-big.count(big[-1]))        
    return 


caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
