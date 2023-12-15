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
    # print(n, nums)
    cache = defaultdict(int)
    #某一个元素，所有的都在cache里了，可以
    for i in range(n):
        find = True
        for j in range(1,nums[i][0] + 1):
            # print(cache, nums[i][j])
            if nums[i][j] not in cache:
                find = False
            cache[nums[i][j]] += 1
        if find:
            print("YES")
            return 
    #每一位的个数都大于1，YES
    for i in range(n):
        find = True
        for j in range(1,nums[i][0] + 1):
            if cache[nums[i][j]] == 1:
                find = False
        if find:
            print("YES")
            return 
    print("NO")
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = []
    for j in range(n):
        nums.append(li())
    main(n, nums)

   
