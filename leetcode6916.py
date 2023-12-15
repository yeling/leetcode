
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

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

ps = getAllPrimes(10**6)

def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

class Solution:
    #TLE 499 / 554
    def findPrimePairs2(self, n: int) -> List[List[int]]:    
        ps = getAllPrimes(n)
        print(len(ps))
        ans = []
        for i in range(len(ps)):
            for j in range(i,len(ps)):
                if ps[i] + ps[j] == n:
                    ans.append([ps[i],ps[j]])
                elif ps[i] + ps[j] > n:
                    break
        ans.sort()
        return ans
    
    #TLE 499 / 554
    # 505 / 554 个通过测试用例
    # 508 / 554 个通过测试用例
    def findPrimePairs3(self, n: int) -> List[List[int]]:    
        # print(len(ps))
        ans = []
        for i in range(2,n//2+1):
            if isPrime(i) and isPrime(n-i):
                ans.append([i,n-i])
        ans.sort()   
        return ans
    
    #TLE 499 / 554
    def findPrimePairs(self, n: int) -> List[List[int]]:    
        # ps = getAllPrimes(n)
        # print(len(ps))
        cache = set(ps)
        ans = []
        for i in range(len(ps)):
            if ps[i] > n//2:
                break
            if (n - ps[i]) in cache:
                ans.append([ps[i], n - ps[i]]) 
        ans.sort()
        return ans
    
n = 10000
sol = Solution()
print(sol.findPrimePairs(n))
