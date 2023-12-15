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

#1.获取所有质数因子
#2.计算可以容纳这些质因子的最大N
def getAllfactor(k):
    fac = []
    i = 2 
    y = k
    while i <= y:
        # print(i,y)
        if y % i == 0:
            fac.append(i)
            y = y // i
            i = 2
        elif i > sqrt(y):
            fac.append(y)
            break
        else:
            i += 1
    return fac
def main(n, nums):
    primes = defaultdict(int)
    for v in nums:
        temp = getAllfactor(v)
        for p in temp:
            primes[p] += 1
    ans = 0
    #step 1 相同的两个一组
    for v in list(primes.keys()):
        if primes[v] >= 2:
            ans += primes[v]//2
            if primes[v]%2 == 1:
                primes[v] = 1
            else:
                del primes[v]
    #step 2 剩下来的三个一组
    # print(primes)
    ans += len(primes)//3
    print(ans)
    
    # print(primes)
    return 

# print(getAllfactor(420))

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    main(n, nums)
   
