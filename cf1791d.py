# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main(all):
    for n,s in all:
        cache = [[0] * 26 for _ in range(n + 1)]
        for i,v in enumerate(s):
            for j in range(26):
                cache[i + 1][j] = cache[i][j]
            cache[i + 1][ord(v) - 97] += 1
        ans = 0
        for i in range(n):
            off = [cache[n][j] - cache[i + 1][j] for j in range(26)]
            temp = 26 - cache[i + 1].count(0) + 26 - off.count(0)
            ans = max(ans, temp)
        print(ans)
    return 

caseNum = int(input())
all = []
for i in range(0, caseNum):
    n = int(input())
    s = input()
    all.append([n,s])
    # main(n, s)
main(all)
   
