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
    ac = s.count('A')
    bc = s.count('B')
    if ac > bc and s[-1] == 'A':
        print('A')
        return
    elif ac < bc and s[-1] == 'B':
        print('B')
        return

    for x in range(2,21):
        aw, bw = 0,0
        ac, bc = 0,0
        last = -1
        for i in range(n):
            if s[i] =='A':
                ac += 1
            elif s[i] == 'B':
                bc += 1
            
            if ac == x:
                aw += 1
                ac = 0
                bc = 0
                last = 'A'
            elif bc == x:
                bw += 1
                ac = 0
                bc = 0
                last = 'B'

        if  ac == 0 and bc == 0:
            # print(s, x, aw, bw, ac, bc)
            if aw > bw and last == 'A':
                print('A')
                return
            elif aw < bw and last == 'B':
                print('B')
                return
    print('?')

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    s = input()
    solve(n, s)

   
