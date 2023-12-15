# auther yeling
from typing import List
from bisect import *
from collections import *

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = [int(v) for v in input().split(' ')]
    #
    preOne = [0] * n
    afterZero = [0] * n
    res = 0
    for i, v in enumerate(nums):
        if v == 1:
            preOne[i] = preOne[i-1] + 1
        elif v == 0:
            preOne[i] = preOne[i-1]
            res += preOne[i]
    # print(res)
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            if i == n - 1:
                afterZero[i] = 1
            else:
                afterZero[i] = afterZero[i + 1] + 1
        elif nums[i] == 1 and i != n - 1:
            afterZero[i] = afterZero[i + 1]
    maxDiff = 0
    maxRes = res
    # print(preOne, afterZero)
    for i in range(n):
        # 0 -> 1
        if nums[i] == 0:
            tempDiff = 0
            if i != n - 1:
                tempDiff += afterZero[i+1]
            if i != 0:
                tempDiff -= preOne[i-1]
            maxDiff = max(maxDiff, tempDiff)
        else:
            tempDiff = 0
            if i != n - 1:
                tempDiff -= afterZero[i+1]
            if i != 0:
                tempDiff += preOne[i-1]
            maxDiff = max(maxDiff, tempDiff)
    res += maxDiff
    print(res)
