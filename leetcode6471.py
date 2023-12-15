
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
    def makeTheIntegerZero2(self, num1: int, num2: int) -> int:    
        if num1 < num2:
            return -1
        ans = 0
        cnt = 0 
        while num1 > num2 and cnt < 10:
            cnt += 1
            ans += 1
            diff = num1 - num2
            num1 = diff - diff & (-diff)
            if num1 == 0:
                break
            print(num1)
        
        return ans
    
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:    
        if num1 < num2:
            return -1
        k = 0
        while True:
            x = num1 - k * num2
            if x < k:
                return -1
            if x.bit_count() <= k:
                return k
            k += 1
        
        return 

def f(diff):
    return (diff &(-diff))
# print(f(5))    
# print(f(6))

num1 = 3
num2 = -2
sol = Solution()
print(sol.makeTheIntegerZero(num1, num2))
