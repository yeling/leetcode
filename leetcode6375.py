
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
import string

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def addMinimum(self, word: str) -> int:
        pre = ''
        ans = 0
        for v in word:
            if v == 'a':
                if pre == '':
                    pre = v 
                elif pre == 'a':
                    ans += 2
                elif pre == 'b':
                    ans += 1
                elif pre == 'c':
                    pre = v
            elif v == 'b':
                if pre == '':
                    ans += 1
                elif pre == 'a':
                    pre = v
                elif pre == 'b':
                    ans += 2
                elif pre == 'c':
                    ans += 1
                    
            elif v == 'c':
                if pre == '':
                    ans += 2
                elif pre == 'a':
                    ans += 1
                elif pre == 'b':
                    pre = v
                elif pre == 'c':
                    ans += 2
            pre = v
                    
        if pre == '':
            ans += 3
        elif pre == 'a':
            ans += 2
        elif pre == 'b':
            ans += 1
        elif pre == 'c':
            ans += 0

        return ans
    
word = "aaaabb"
# word = "abb"
sol = Solution()
print(sol.addMinimum(word))
