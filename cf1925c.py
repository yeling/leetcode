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

def solve(n, k, m, s):
    cache = [0] * k
    curr = 0
    ans = ''
    for i,v in enumerate(s):
        cache[ord(v) - ord('a')] = 1
        if sum(cache) == k:
            ans += v
            curr += 1
            cache = [0] * k
    if curr >= n:
        print(YES)
    else:
        print(NO)
        if sum(cache) == 0:
            ans += 'a'
        else:
            for i in range(k):
                if cache[i] == 0:
                    ans += chr(i + 97)
                    break
        s = len(ans)
        for i in range(s, n):
            ans += 'a'
        print(ans)
        

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,k,m = li()
    s = input()
    solve(n, k, m, s)


   
