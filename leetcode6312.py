
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
    def splitNum(self, num: int) -> int:
        arr = []
        while num > 0:
            arr.append(num%10)
            num //= 10
        arr.sort()
        num1 = 0
        num2 = 0
        index = 0
        while index < len(arr):
            num1 = num1 * 10 + arr[index]
            index += 1
            if index < len(arr):
                num2 = num2 * 10 + arr[index]
                index += 1
        
        # print(arr)
        return num2 + num1
    
num = 2
sol = Solution()
print(sol.splitNum(num))
