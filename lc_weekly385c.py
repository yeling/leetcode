
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
# from sortedcontainers import SortedList


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

all = getAllPrimes(10**6)
ps = set()
for v in all:
    if v > 10:
        ps.add(v)

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        dirs = [[1,0], [-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        m = len(mat)
        n = len(mat[0])
        ans = 0
        cache = defaultdict(int)
        for i in range(m):
            for j in range(n):
                for d in dirs:
                    t = mat[i][j]
                    dx = i + d[0]
                    dy = j + d[1]
                    while dx >= 0 and dx < m and dy >= 0 and dy < n:
                        t = t * 10 + mat[dx][dy]
                        if t in ps:
                            cache[t] += 1
                        dx += d[0]
                        dy += d[1]
        f = 0
        v = -1
        # print(cache)
        for k in cache:
            if cache[k] > f:
                v = k
                f = cache[k]
            elif cache[k] == f and k > v:
                v = k
                

        return v
    
mat = [[1,1],[9,9],[1,1]]
mat = [[9,7,8],[4,6,5],[2,8,6]]
sol = Solution()
print(sol.mostFrequentPrime(mat))
