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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def getAllPrimes(N):
#     prime = [0] * N
    prime = defaultdict(int)
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
        del prime[i]
    return allPrime

def main(n):
    allP = getAllPrimes(n)
    setP = set(allP)
    for p in allP:
        if n%(p * p) == 0:
            q = n //( p * p)
            if q in setP and p != q:
                print(p, q)
                return 

caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
