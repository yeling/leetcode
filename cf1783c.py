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
#1.顺序赢过区
#2.最后不赢，赢后面一个，可以一次性加2
def main(n, m, nums):
    ans = 0
    win = [i for i in range(n)]
    pair = []
    for i,v in enumerate(nums):
        pair.append([v,i])
    pair.sort()
    print(pair)
    for v in pair:
        if m >= v[0]:
            ans += 1
            m -= v[0]
        else:
            v[1] += 1
    pair.sort(key= lambda x:x[1])
    print(pair, ans)
    pos = -1
    for i,v in enumerate(pair):
        if ans >= v[1]:
            pos = i
        else:
            break
    print(n - pos)
    

    return 

# n,m = 4, 4
# nums = [1, 2, 2, 1]
# main(n, m, nums)

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n, m, nums)

   
