# auther yeling
from typing import List
from bisect import *
from collections import *


def main(n, nums):
    res = [0] * n
    preSum = 0
    for i,v in enumerate(nums):
        # print(v, preSum)
        res[i] = v - preSum
        preSum += res[i]
    print(*res)


allnums = int(input())
nums = [int(v) for v in input().split(' ')]
main(allnums, nums)

