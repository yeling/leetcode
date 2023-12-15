
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
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0]*n
        cache = set()
        cnt = 0
        left = []
        for i in range(n):
            cache.add(A[i])
            left.append(B[i])
            for j in range(len(left) - 1, -1, -1):
                if left[j] in cache:
                    left.pop(j)
                    cnt += 1
            ans[i] = cnt
            # print(left)



        return ans
    
A = [1,3,2,4]
B = [3,1,2,4]
A = [2,3,1]
B = [3,1,2]
sol = Solution()
print(sol.findThePrefixCommonArray(A,B))
