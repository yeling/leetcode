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

def solve(n, ch, s):
    sa = s.split()
    # print(sa)
    # CDHS
    keys = "CDHS"
    cache = defaultdict(list)
    for v in keys:
        cache[v] = [0] * 10
    
    for v in sa:
        cache[v[1]][int(v[0])] += 1
    
    # print(cache)
    ans = []
    left = []
    for k in keys:
        if k != ch:
            for i in range(2,10):
                j = i + 1
                while cache[k][i] > 0 and j < 10:
                    if cache[k][j] > 0:
                        if cache[k][j] >= cache[k][i]: 
                            ans += [str(i) + k,  str(j) + k] * cache[k][i]
                            cache[k][j] -= cache[k][i]
                            cache[k][i] = 0
                        else:
                            ans += [str(i) + k, str(j) + k] * cache[k][j]
                            cache[k][i] -= cache[k][j]
                            cache[k][j] = 0
                    j += 1
                if cache[k][i] > 0:
                    left += [str(i) + k] * cache[k][i]
    # print(left)
    k = ch
    tr = []
    for i in range(2,10):
        j = i + 1
        while cache[k][i] > 0 and j < 10:
            if cache[k][j] > 0:
                if cache[k][j] >= cache[k][i]: 
                    tr += [str(i) + k,  str(j) + k] * cache[k][i]
                    cache[k][j] -= cache[k][i]
                    cache[k][i] = 0
                else:
                    tr += [str(i) + k, str(j) + k] * cache[k][j]
                    cache[k][i] -= cache[k][j]
                    cache[k][j] = 0
            j += 1
    i = 0
    j = 2
    for i in range(len(left)):
        while j < 10 and cache[k][j] == 0:
            j += 1
        if j < 10 and cache[k][j] > 0:
            ans += [left[i], str(j) + k]
            cache[k][j] -= 1
        elif len(tr) > 0:
            ans += [left[i], tr[-1]]
            tr = tr[:-1]
    if len(tr) > 0:
        ans += tr

    if len(ans) != 2 * n:
        print("IMPOSSIBLE")
    else:
        for i in range(0, n):
            print(ans[2*i], ans[2*i + 1])
           





                    

    

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    ch = input()
    s = input()
    solve(n, ch, s)

   
