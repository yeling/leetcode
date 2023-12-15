
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
def isPrime(n):
    if(n == 1):
        return False
    m = int(sqrt(n))
    for i in range(2,m + 1):
        if n%i == 0:
            return False
    return True

def ExpGcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ExpGcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q

def Inv( a,  n): 
    x, y, q = ExpGcd(a, n) 
    x = (x % n + n) % n
    return x

class Solution:
    # 1564 / 1566 个通过测试用例
    def constructProductMatrix2(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        dst = 1
        for i in range(n):
            for j in range(m):
                dst *= grid[i][j]
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = (dst )//grid[i][j]%MOD
            
        return ans

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n = len(grid)
        m = len(grid[0])
        dst = 1
        pre = [1] * ( n * m + 1)
        sufix = [1] * ( n * m + 1)

        for i in range(n):
            for j in range(m):
                pre[i * m + j + 1] = (pre[i * m + j] * grid[i][j])%MOD
        
        for i in range(n - 1, -1, -1):
            for j in range(m-1, -1, -1):
                sufix[i * m + j] = (sufix[i * m + j + 1] * grid[i][j])%MOD
        
        # print(pre, sufix)
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = pre[i * m + j] * sufix[i * m + j + 1] %MOD
            
        return ans
    
# grid = [[1,2],[3,4]]
grid = [[12345],[2],[1]]
sol = Solution()
print(sol.constructProductMatrix2(grid))
print(sol.constructProductMatrix(grid))
