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

def main(n, nums):
    if max(nums) == 0:
        print('No')
        return 
    ans = []
    pos = [v for v in nums if v >= 0]
    neg = [v for v in nums if v < 0]
    # print(pos, neg)
    i = 0
    j = 0
    curr = 0
    while i < len(pos) or j < len(neg):
        if curr <= 0:
            ans.append(pos[i])
            curr += pos[i]
            i += 1 
        else:
            ans.append(neg[j])
            curr += neg[j]
            j += 1    
    print('Yes')
    print(*ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
