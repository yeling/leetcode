# auther yeling
from typing import List
from bisect import *
from collections import *

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = [int(v) for v in input().split(' ')]
    # print(n ,nums)
    m1, m2 = 0,0
    for v in nums:
        if v > m1:
            m2 = m1
            m1 = v 
        elif v > m2:
            m2 = v
    res = [0] * n
    for i,v in enumerate(nums):
        if v == m1:
            res[i] = v - m2
        else:
            res[i] = v - m1
    print(*res)
   
