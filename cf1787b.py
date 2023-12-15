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
    return allPrime

def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

# allPrime = []
allPrime = getAllPrimes(10 ** 5)
#TLE
def main(n):
    # print(allPrime)
    # print(len(allPrime), allPrime[-1])
    cache = defaultdict(int)
    num = n
    s = 0
    while allPrime[s] <= num:
        while num%allPrime[s] == 0:
            cache[allPrime[s]] += 1
            num//=allPrime[s]
            # print(num, allPrime[s])
        s += 1
        if isPrime(num):
            cache[num] += 1
            break
    # print(cache, num)
    all = []
    for k in cache:
        all.append((cache[k],k))
    all.sort()
    # print(all)
    preMul = [1] * (len(all) + 1)
    for i,(cnt,k) in enumerate(all):
        # print(i, k, cnt)
        preMul[i + 1] = k * preMul[i]
    ans = 0
    tempS = 0
    for i,(cnt,k) in enumerate(all):
        cnt -= tempS
        ans += preMul[len(all)]//preMul[i] * cnt
        tempS += cnt
        
    print(ans)
        
    return 

# main(10)
# main(864)
# main(10886400)
# main(999999018)
# main(2)
caseNum = int(input())
for i in range(0, caseNum):
    n = int(input())
    main(n)
   
