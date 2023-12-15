
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
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num1 = 0
        for i in range(len(arr1)):
            if arr1[-1-i] == 1:
                num1 += ((-2) ** i)
        num2 = 0
        for i in range(len(arr2)):
            if arr2[-1-i] == 1:
                num2 += ((-2) ** i)
        # print(num1, num2)
        ans = []
        s = num1 + num2

        while s != 0:
            curr = s%(-2)
            if curr == -1:
                curr = 1
            ans.insert(0,curr)
            s = (s - curr)// -2
        if len(ans) == 0:
            ans = [0]


        return ans
    
arr1 = [1,1,1,1,1]
arr2 = [1,0,1]
sol = Solution()
print(sol.addNegabinary(arr1, arr2))
