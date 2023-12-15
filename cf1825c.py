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

def main(n, m, nums):
    cache = defaultdict(int)
    for v in nums:
        cache[v] += 1
    #
    all = list(cache.keys())
    all.sort()
    if cache[-2] != 0:
        all = all[1:]
    if cache[-1] != 0:
        all = all[1:]

    ans = max(min(m,cache[-1] + len(all)), min(m,cache[-2] + len(all)))
    for i,v in enumerate(all):
        temp = min(v-1,cache[-1] + i) + 1 + min(m - v, cache[-2] + len(all) - 1 - i)
        ans = max(ans, temp)
        # print(v)
    

    # print(all)
    #ans = min(m, cache[-1] + cache[-2] + len(cache) - 2)

    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    main(n, m, nums)
   
