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

def main(n:int, nums):
    odd = []
    even = []
    for i,v in enumerate(nums):
        if v%2 == 0:
            even.append(i+1)
        else:
            odd.append(i+1)
    if len(odd) >= 3:
        print('Yes')
        print(*odd[:3])
    elif len(odd) >= 1 and len(even) >= 2:
        print('Yes')
        ans = [odd[0], even[0], even[1]]
        print(*ans)
    else:
        print('No')
    return 

def main2(n:int, nums):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if (nums[i] + nums[j] + nums[k])%2 == 1:
                    ans = [i+1, j + 1, k + 1]
                    print('YES')
                    print(*ans)
                    return
    print('No')
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
