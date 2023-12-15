
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
    
    #31 / 49 个通过测试用例
    def divisibilityArray2(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        for i in range(n):
            temp = word[:i+1]
            if int(temp)%m == 0:
                ans[i] = 1
        return ans
    
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        ans = [0] * n
        left = 0
        for i in range(n):
            temp = left * 10 + int(word[i])
            if temp%m == 0:
                ans[i] = 1
                left = 0
            else:
                left = temp%m
        return ans
    
word = "12355421"
m = 4
# word = "1010"
# m = 10
sol = Solution()
print(sol.divisibilityArray2(word, m))
print(sol.divisibilityArray(word, m))




