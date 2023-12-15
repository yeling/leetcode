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
    ans = []
    index = [0] * n
    for i in range(n):
        temp = defaultdict(int)
        for j in range(n):
            if len(ans) > 0 and ans[-1] == nums[j][index[j]]:
                index[j] += 1
            if index[j] < n - 1:
                temp[nums[j][index[j]]] += 1
        for k in temp:
            if temp[k] != 1:
                ans.append(k)
                break
        # print(temp, ans, index)
    print(*ans) 
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = []
    for j in range(n):
        nums.append(li())
    main(n, nums)

