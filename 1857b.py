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
    curr = 0
    pos = -1
    for i in range(len(s) -1, -1, -1):
        temp = int(s[i]) + curr
        if temp >= 5:
            curr = 1
            pos = i
        else:
            curr = 0
    ans = ''
    if pos == 0:
        ans = '1' + '0'*len(s)
    elif pos == -1:
        ans = s
    else:
        ans = s[0:pos - 1] + str(int(s[pos-1]) + 1) + '0'*(len(s) - pos)
    print(ans)
        

    return 

caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)

   
