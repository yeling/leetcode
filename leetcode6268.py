
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
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def getAllF(num):
            ans = []
            while num >= 1:
                ans.append(num)
                num = num//2
            return ans
        ret = []
        for v in queries:
            f0 = getAllF(v[0])
            f1 = getAllF(v[1])
            i = len(f0) - 1
            j = len(f1) - 1
            while i >= 0 and j >= 0:
                if f0[i] == f1[j]:
                    i -= 1
                    j -= 1
                else:
                    break
            ret.append(i + 1 + j + 1 + 1)
        return ret
    
n = 3
queries = [[5,3],[4,7],[2,3]]
# n = 2
# queries = [[1,2]]
sol = Solution()
print(sol.cycleLengthQueries(n,queries))
