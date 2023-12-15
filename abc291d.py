# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 998244353
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n, nums):
    # print(n, nums)
    cache = [[0]*2 for _ in range(n+1)]
    for i, [a,b] in  enumerate(nums):
        if i == 0:
            if a == b:
                cache[i][0] = 1
                cache[i][1] = 0
            else:
                cache[i][0] = 1
                cache[i][1] = 1
        else:
            if a != nums[i-1][0]:
                cache[i][0] += cache[i - 1][0] 
            if a != nums[i-1][1]:
                cache[i][0] += cache[i - 1][1] 
            if a != b:
                if b !=  nums[i-1][0]:
                    cache[i][1] += cache[i - 1][0] 
                if b !=  nums[i-1][1]:
                    cache[i][1] += cache[i - 1][1]
            cache[i][0] = cache[i][0]%MOD
            cache[i][1] = cache[i][1]%MOD
            if cache[i][0] == 0 and cache[i][1] == 0:
                print(0)
                return 
            

    if nums[-1][0] == nums[-1][1]:
        print((cache[n-1][0])%MOD)
    else:
        print((cache[n-1][0] + cache[n-1][1])%MOD)

    return


def main(n, nums):
    # print(n, nums)
    cache = [[0]*2 for _ in range(n+1)]
    for i, [a,b] in  enumerate(nums):
        if i == 0:
            if a == b:
                cache[i][0] = 1
                cache[i][1] = 1
            else:
                cache[i][0] = 1
                cache[i][1] = 1
        else:
            if a != nums[i-1][0]:
                cache[i][0] += cache[i - 1][0] 
            if a != nums[i-1][1]:
                cache[i][0] += cache[i - 1][1] 
            if a != b:
                if b !=  nums[i-1][0]:
                    cache[i][1] += cache[i - 1][0] 
                if b !=  nums[i-1][1]:
                    cache[i][1] += cache[i - 1][1]
            cache[i][0] = cache[i][0]%MOD
            cache[i][1] = cache[i][1]%MOD
            if cache[i][0] == 0 and cache[i][1] == 0:
                print(0)
                return 
            
    print((cache[n-1][0] + cache[n-1][1])%MOD)

    return



n = int(input())
nums = []
for i in range(0, n):
    nums.append(li())
main(n, nums)

