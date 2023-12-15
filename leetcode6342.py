
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
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ap = []
        matp = []
        for i,v in enumerate(arr):
            ap.append((v,i))
        for i in range(m):
            for j in range(n):
                matp.append((mat[i][j],i,j))
        ap.sort()
        matp.sort()
        # print(ap)
        # print(matp)
        arrp = [0] * (len(arr))
        for i,v in enumerate(ap):
            arrp[v[1]] = (matp[i][1],matp[i][2])

        arrow = [0]*m
        col = [0]*n
        # print(arrp)
        for i,v in enumerate(arrp):
            arrow[v[0]] += 1
            col[v[1]] += 1
            if arrow[v[0]] == n or col[v[1]] == m:
                return i

        return
    
arr = [1,3,4,2]
mat = [[1,4],[2,3]]
arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]
sol = Solution()
print(sol.firstCompleteIndex(arr, mat))
