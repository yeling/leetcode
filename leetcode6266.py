
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
    def smallestValue2(self, n: int) -> int:
        def getAllPrimesSum(N):
            # print('getAllPrimesSum' , N)
            v = N
            ans = 0
            temp = 2
            while v >= temp:
                while v%temp == 0:
                    v = v//temp
                    ans += temp
                temp += 1
            return ans
        while True:
            s = getAllPrimesSum(n)
            if s == n:
                break
            else:
                n = s
        return n
    
    def smallestValue(self, n: int) -> int:
        def getAllPrimesSum(N):
            # print('getAllPrimesSum' , N)
            v = N
            ans = 0
            temp = 2
            while v >= temp * temp:
                while v%temp == 0:
                    v = v//temp
                    ans += temp
                temp += 1
            if v > 1:
                ans += v
            return ans
        while True:
            s = getAllPrimesSum(n)
            if s == n:
                break
            else:
                n = s
        return n
    
    
n = 108
sol = Solution()
print(sol.smallestValue2(n))

print(sol.smallestValue(n))
