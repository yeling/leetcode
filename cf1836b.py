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
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def solve(n, k, g):
    t = k * g
    ans = ((g - 1)//2) * (n - 1)
    if ans > t:
        print(t)
        return
    left = (t - ans)%g
    if left%g >= ((g + 1)//2):
        ans += left%g - g
    else:
        ans += left%g 
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,g = li()
    solve(n, k, g)


   
