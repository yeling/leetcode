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

def solve(n, a, b):
    a.sort()
    b.sort()
    # print(a, b)
    r = n - 1
    ans = 1
    for i in range(n-1, -1, -1):
        if a[i] <= b[i]:
            ans = 0
            break
        nextr = r 
        for j in range(r,i - 1,-1):
            if b[j] < a[i]:
                nextr = j
                break
        r = nextr
        diff = r - i
        if i == n - 1:
            ans = 1
        else:
            ans = (ans + diff * ans)%MOD
        # print(i, a[i], ans,diff)
        
    
    print(ans%MOD)
    return 

def check(n, a, b):
    a.sort()
    b.sort()
    cnt = 0
    for p in permutations(a):
        flag = True
        for i,v in enumerate(p):
            if v > b[i]:
                continue
            else:
                flag = False
                break
        if flag:
            print(p, cnt)
            cnt += 1
    return


a = [2, 5, 7, 8, 11, 10]
b = [4, 1, 5, 6, 3, 1]
# check(len(a), a, b)
# solve(len(a), a, b)

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    a = li()
    b = li()
    solve(n, a, b)
