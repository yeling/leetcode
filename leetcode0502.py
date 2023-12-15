
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
    def printBin(self, num: float) -> str:
        cnt = 0
        start = num
        while start - int(start) > 0 and cnt <= 30:
            start = start * 2
            cnt += 1
        # print(cnt, start)
        if cnt <= 30:
            ans = bin(int(start))[2:]
            return '0.' + '0'*(cnt - len(ans)) + ans
        else:
            return 'ERROR'
            
        
    
# num = 0.625
num = 0.125
sol = Solution()
print(sol.printBin(num))
