
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        m = len(queries)
        color = [0] * n
        ans = [0] * m
        diff = 0
        for j,(i,c) in  enumerate(queries):
            if i + 1 < n and color[i+1] != 0:
                if color[i + 1] == color[i]:
                    diff -= 1
                if color[i + 1] == c:
                    diff += 1

            if i - 1 >= 0 and color[i - 1] != 0:
                if color[i - 1] == color[i]:
                    diff -= 1
                if color[i - 1] == c:
                    diff += 1
            color[i] = c
            ans[j] = diff

        return ans
    
n = 4
queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
n = 1
queries = [[0,100000]]
sol = Solution()
print(sol.colorTheArray(n, queries))
