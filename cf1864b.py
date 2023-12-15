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

def solve2(n, k, s):
    cnt = [0]*26
    for v in s:
        cnt[ord(v) - 97] += 1
    ans = ''
    for i,v in enumerate(cnt):
        ans += chr(i + 97)*v

    print(ans)
    return 

def solve(n, k, s):
    cache = [v for v in s]
    if k % 2 == 0:
        cache.sort()
        print(''.join(cache))
    else:
        odd = []
        even = []
        for i,v in enumerate(s):
            if i%2 == 0:
                even.append(v)
            else:
                odd.append(v)
        even.sort()
        odd.sort()
        ans = ''
        l = 0
        r = 0
        while l < len(even) or r < len(odd):
            if l < len(even):
                ans += even[l]
            if r < len(odd):
                ans += odd[r]
            l += 1
            r += 1
        print(ans)




    
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    s = input()
    solve(n, k, s)

   
