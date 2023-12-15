
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
    def minimumSwap(self, s1: str, s2: str) -> int:
        a = s1.count('x')
        c = s2.count('x')
        if (a + c)%2 != 0:
            return -1
        diff = 0
        n = len(s1)
        #记录 xy 不同的数量，yx出现的数量
        cnt0 = 0
        cnt1 = 0
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    cnt0 += 1
                elif s1[i] == 'y':
                    cnt1 += 1
        ans = cnt0//2 + cnt1//2 + cnt0%2 + cnt1%2
        return ans
    
s1 = "xyxy"
s2 = "yxyx"
sol = Solution()
print(sol.minimumSwap(s1,s2))
