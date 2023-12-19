
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

def Exp(a, n, mod):
    ans = 1
    while n != 0:
        if n & 1 != 0:
            ans = ans * a %mod
        a = a * a % mod
        n >>= 1
    return ans

def Inv2(a, p):
    return Exp(a, p-2, p)


class Solution:
    # 22 / 1000 
    # 35 / 1000
    # 48 / 1000 
    # 329 / 1000
    # AC
    def numberOfSequence2(self, n: int, sick: List[int]) -> int:  
        if len(sick) == n:
            return 0
        ans = 1
        base = 1
        pow = [1] * (n + 1)
        for i in range(2, n + 1):
            pow[i] = (pow[i - 1] * i)%MOD
        left = n - len(sick)
        # print(pow)
        for i in range(0,len(sick)):            
            if i == 0:
                if sick[0] != 0:
                    le = sick[0] - 1                    
                    ans *= pow[left] * Inv2(pow[le + 1], MOD) * Inv2(pow[left - (le + 1)], MOD)
                    left = left - (le + 1)
            else:        
                le = sick[i] - sick[i - 1] - 2
                # print(le)
                if le >= 0:
                    ans *= (1 << le)%MOD
                    #C(b,a)
                    #print(left, pow[left], Inv2(pow[le + 1], MOD) , Inv2(pow[left - (le + 1)], MOD))
                    ans *= pow[left] * Inv2(pow[le + 1], MOD) * Inv2(pow[left - (le + 1)], MOD)
                    left = left - (le + 1)                    
            ans %= MOD
        #        print(i, ans, left)
        
        return ans%MOD
    # 3032ms
    # 2784ms    
    def numberOfSequence(self, n: int, sick: List[int]) -> int:  
        if len(sick) == n:
            return 0
        ans = 1
        base = 1
        pow = [1] * (n + 1)
        inv = [0] * (n + 1)
        for i in range(2, n + 1):
            pow[i] = (pow[i - 1] * i)%MOD

        left = n - len(sick)
        # print(pow)
        for i in range(0,len(sick)):            
            if i == 0:
                if sick[0] != 0:
                    le = sick[0]
                    if inv[le] == 0:
                        inv[le] = Inv2(pow[le], MOD)
                    if inv[left - le] == 0:
                        inv[left - le] = Inv2(pow[left - le], MOD)

                    ans *= pow[left] * inv[le] * inv[left - le]
                    left = left - le
            else:        
                le = sick[i] - sick[i - 1] - 1
                # print(le)
                if le >= 1:
                    ans *= (1 << (le - 1))%MOD
                    #C(b,a)
                    #print(left, pow[left], Inv2(pow[le + 1], MOD) , Inv2(pow[left - (le + 1)], MOD))
                    if inv[le] == 0:
                        inv[le] = Inv2(pow[le], MOD)
                    if inv[left - le] == 0:
                        inv[left - le] = Inv2(pow[left - le], MOD)

                    ans *= pow[left] * inv[le] * inv[left - le]
                    left = left - le                    
            ans %= MOD
        #        print(i, ans, left)
        
        return ans%MOD
    
n = 5
sick = [0,2]
# n = 5
# sick = [2]

n = 2
sick = [1]

sol = Solution()
print(sol.numberOfSequence(n, sick))


