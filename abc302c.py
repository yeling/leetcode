# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def solve(n, m, arr):
    dp = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            diff = 0
            for k in range(m):
                if arr[i][k] == arr[j][k]:
                    continue
                else:
                    diff += 1
            if diff == 1:
                dp[i][j] = True
                dp[j][i] = True
    for v in permutations(range(n)):
        flag = True
        for i in range(1,n):
            if dp[v[i]][v[i-1]] == True:
                continue
            else:
                flag = False
                break
        if flag:
            print(YES)
            return
    print(NO)
    return 


n,m = li()
arr = []
for _ in range(n):
    arr.append(input())
solve(n, m, arr)