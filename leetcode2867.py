
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

prime = [0] * (10 ** 5)


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

# getAllPrimes(10**5)

class Solution:
    #树形d，后序遍历，先子节点后父节点
    def countPaths(self, n: int, edges: List[List[int]]) -> int:    
        allPrimes = set(getAllPrimes(n + 1))
        vis = [False] * (n + 1)
        out = [[] for _ in range(n + 1)]
        for u,v in edges:
            out[u].append(v)
            out[v].append(u)
        ans = 0
        #[0,1] 0个质数，1个质数
        def dfs(root):
            nonlocal ans
            curr = [0,0]
            rp = root in allPrimes
            vis[root] = True
            for v in out[root]:
                if vis[v] == True:
                    continue
                left = dfs(v)
                if rp:
                    ans += left[0]
                    ans += curr[1] * left[0]
                    curr[1] += left[0]
                else:
                    ans += left[1]
                    ans += left[1] * curr[0] + left[0] * curr[1]
                    curr[0] += left[0]
                    curr[1] += left[1]
            if rp:
                curr[0] = 0
                curr[1] += 1
            else:
                curr[0] += 1
            # print(root, ans, curr)

            return curr
        
        dfs(1)
        return ans
    

n = 5
edges = [[1,2],[1,3],[2,4],[2,5]]

# n = 6
# edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
sol = Solution()
print(sol.countPaths(n, edges))
