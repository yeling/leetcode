
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

class Solution:
    # 1005 / 1040 个通过测试用例
    # gcd
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        cache = [list() for _ in range(k)]
        vis = [False] * n
        i = 0
        while i < n:
            if vis[i] == True:
                i += 1
                continue
            temp = i
            while vis[temp] == False:
                vis[temp] = True
                cache[i%k].append(arr[temp])
                temp += k
                temp %= n
            i += 1
            # print(cache)
        ans = 0
        for ns in cache:
            if(len(ns) > 0):
                ns.sort()
                # print(ns)
                av = ns[len(ns)//2]
                for v in ns:
                    ans += abs(v - av)


        return ans
    
# arr = [2,5,5,7]
# k = 3
arr = [1,4,1,3]
k = 2

arr = [2,10,9]
k = 1

arr = [6,2,8,5,7,10]
k = 4

sol = Solution()
print(sol.makeSubKSumEqual(arr, k))
