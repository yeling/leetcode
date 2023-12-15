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

def main(n, m, nums):
    ans = 0
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(nums[j][i])
        temp.sort()
        
        pre = 0
        for i,k in enumerate(temp):
            if i == 0:
                pre = k
            else:
                ans += i * k - pre
                pre += k 
        # print(temp, pre, ans)

    print(ans)

    return 

caseNum = int(input())
for i in range(0, caseNum):
    n, m = li()
    nums = []
    for _ in range(n):
        nums.append(li())
    main(n, m, nums)
