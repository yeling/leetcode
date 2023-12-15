
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

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:   
        n = len(parent)
        ans = n
        cache = [[0]*26 for _ in range(n)]
        child = [[] for _ in range(n)]
        for i in range(1,n):
            child[parent[i]].append(i)
        # print(child)
        def dfs(index, path):
            if len(child[index]) == 0:
                return
            for v in child[index]:
                temp = path[:]
                temp[ord(s[v]) - 97] += 1
                cache[v] = temp
                dfs(v, temp)
            return
        dfs(0, [0]*26)
        # print(cache)
        ans = 0
        for i in range(1,n):
            

        return
    
parent = [-1,0,0,1,1,2]
s = "acaabc"
sol = Solution()
print(sol.countPalindromePaths(parent, s))
