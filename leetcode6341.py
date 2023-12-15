
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
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        s1 = 0
        s2 = 0
        for i in range(n):
            if i >= 1 and player1[i-1] == 10 or i >= 2 and player1[i-2] == 10:
                s1 += 2 * player1[i]
            else:
                s1 += player1[i]

            if i >= 1 and player2[i-1] == 10 or i >= 2 and player2[i-2] == 10:
                s2 += 2 * player2[i]
            else:
                s2 += player2[i]
        # print(s1, s2)
        ans = 0
        if s1 > s2:
            ans = 1
        elif s1 == s2:
            ans = 0
        else:
            ans = 2
        return ans
    
player1 = [3,5,7,6]
player2 = [8,10,10,2]
player1 = [4,10,7,9]
player2 = [6,5,2,3]
sol = Solution()
print(sol.isWinner(player1, player2))
