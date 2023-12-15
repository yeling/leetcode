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
input = sys.stdin.readline
print = sys.stdout.write
 
# input = lambda: sys.stdin.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())
 
def solve(s):
    #(pos, letter)
    mi = deque()
    ma = deque()
    for i,v in enumerate(s):
        if 97 <= ord(v) <= 122:
            if v == 'b':
                if len(mi) > 0:
                    mi.pop()
            else:
                mi.append((i, v))
        else:
            if v == 'B':
                if len(ma) > 0:
                    ma.pop()
            else:
                ma.append((i, v))
    left = ma + mi
    left = sorted(left)
    # print(left)
    ans = ''
    for v in left:
        ans += v[1]
    print(ans)
    return 
 
caseNum = int(input())
for i in range(0, caseNum):
    s = input()
    solve(s)