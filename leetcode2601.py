
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



class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        allPrimes = getAllPrimes(1100)
        pre = 0
        # print(allPrimes)
        for v in nums:
            if v == 1 and v > pre:
                pre = v
                continue

            sub = -1
            for i,p in enumerate(allPrimes):
                if p + pre >= v:
                    sub = i - 1
                    break
            if sub == -1 and v <= pre:
                return False
            else:
                if sub != -1:
                    pre = v - allPrimes[sub]
                else:
                    pre = v
            # print(pre)

        
        return True
    
nums = [1,2,4]
nums = [998,2]
sol = Solution()
print(sol.primeSubOperation(nums))
