
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
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i,n):
                temp = s[i:j+1]
                # print(temp)
                if temp.count('0') == temp.count('1') and (j - i + 1)%2 == 0:
                    flag = True
                    for k in range(len(temp)//2):
                        if temp[k] == '1':
                            flag = False
                            break
                    if flag:
                        ans = max(ans, j - i + 1)

        return ans
    
s = "01000111"
s = "00111"
s = "111"
sol = Solution()
print(sol.findTheLongestBalancedSubstring(s))
