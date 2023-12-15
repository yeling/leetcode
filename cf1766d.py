# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import time

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7


def mi(): return map(int, input().split())
def li(): return list(mi())


def main2(x, y):
    # print(x,y)
    if abs(x-y) == 1:
        print(-1)
        return
    ans = 0
    while gcd(x, y) == 1:
        print(x, y)
        ans += 1
        x += 1
        y += 1
    # print(x,y, gcd(x,y))
    print(ans)


def getAllFactor(num):
    ans = []
    i = 2
    while i * i < num:
        if num % i == 0:
            ans.append(i)
            while num % i == 0:
                num //= i
        i += 1
    ans.append(num)
    return ans

N = 10 ** 7
prime = [0] * N


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
            print(allPrime, prime)
    return allPrime

def init():
    # N = 10 ** 2
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
        

def main(x, y):
    # print(x,y)
    if abs(x-y) == 1:
        print(-1)
        return
    elif gcd(x, y) == 1:
        dst = abs(x - y)
        ans = dst
        while dst > 1:
            p = prime[dst]
            dst = dst // p
            ans = min(ans, p - x % p)
        print(ans)
    else:
        print(0)

start = time.time()
# init()
# main(13,37)
allPrimes = getAllPrimes(30)
print(len(allPrimes))

# caseNum = int(input())
# for i in range(0, caseNum):
#     x,y = li()
#     main(x,y)

end = time.time()
print("used %.2f second "%(end-start))

