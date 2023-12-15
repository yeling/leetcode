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

def solve(n, nums):
    vis = [False] * (n + 1)
    mi = 1
    ma = 0
    i = 1
    while i < n + 1:
        if vis[i] == False:
            j = i
            cnt = 0
            while vis[j] == False:
                # print(j)
                cnt += 1
                vis[j] = True
                j = nums[j - 1]
            # print(i, j)
            if j == i and cnt > 2:
                mi += 1
            ma += 1
        i += 1
    print(mi, ma)



    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve(n, nums)
   
