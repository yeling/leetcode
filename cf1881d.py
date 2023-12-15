# auther yeling
import sys
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from heapq import *
import string
from os import path

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7
YES="Yes"
NO="No"


# for I/O for local system
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    # sys.stdout = open("output.txt","w")

# For fast I/O
# input = sys.stdin.buffer.readline
# input = sys.stdin.readline
# print = sys.stdout.write

input = lambda: sys.stdin.buffer.readline().rstrip()
si = lambda :int(input())
mi = lambda :map(int,input().split())
li = lambda :list(mi())

#1.获取所有质数因子
#2.计算可以容纳这些质因子的最大N
def getAllfactor(num):
    ans = defaultdict(int)
    i = 2
    while i * i <= num:
        if num % i == 0:
            while num % i == 0:
                num //= i
                ans[i] += 1
        i += 1
    if num != 1:
        ans[num] += 1

    return ans
# factors = defaultdict(list)
# for i in range(2, 10 ** 6 + 1):
#     factors[i] = getAllfactor(i)

def solve2(n, nums):
    ma = max(nums)
    if ma == 1:
        print(YES)
        return
    cache = [0] * (max(nums) + 1)
    for v in nums:
        ps = getAllfactor(v)
        for p in ps:
            cache[p] += ps[p]
    for v in cache:
        if v % n != 0:
            print(NO)
            return
    print(YES)
    return 

def getAllPrimes(N):
    prime = [0] * N
    allPrime = []
    for i in range(2, N):
        if prime[i] == 0:
            allPrime.append(i)
            prime[i] = i
        for v in allPrime:
            if i * v >= N:
                break
            prime[i*v] = v
            if i % v == 0:
                break
    # print(allPrime, prime)
    return allPrime

primes = getAllPrimes(10 ** 6 + 1)
cachePrimes = set(primes)
# print(len(primes))

def solve(n, nums):
    ma = max(nums)
    if ma == 1:
        print(YES)
        return
    cache = [0] * (max(nums) + 1)
    for v in nums:
        if v in cachePrimes:
            cache[v] += 1
            continue
        for p in primes:
            if p*p > v:
                break
            while v%p == 0:
                cache[p] += 1
                v //= p
        # print(v, cache)
    for v in cache:
        if v % n != 0:
            print(NO)
            return
    print(YES)
    return 

def solve3(n, nums):
    ma = max(nums)
    if ma == 1:
        print(YES)
        return
    cache = defaultdict(int)
    for v in nums:
        for p in primes:
            if p*p > v:
                break
            while v%p == 0:
                cache[p^MOD] += 1
                v //= p
        if v in cachePrimes:
            cache[v^MOD] += 1
            continue
        # print(v, cache)
    for v in cache:
        if cache[v] % n != 0:
            print(NO)
            return
    print(YES)
    return 

mxn = 10 ** 6
mxn = 100
factor = [1] * (mxn + 1)
 
def init():
    for i in range(2, mxn + 1):
        if factor[i] != 1:
            continue
        for j in range(i, mxn + 1, i):
            factor[j] = i
init()
print(factor)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    nums = li()
    solve3(n, nums)
   
