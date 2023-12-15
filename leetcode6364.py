
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
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = []
        for i in range(n):
            diff.append((reward1[i] - reward2[i],i))
        diff.sort(reverse=True)
        ans = 0
        for i in range(n):
            if i < k:
                ans += reward1[diff[i][1]]
            else:
                ans += reward2[diff[i][1]]
        # print(diff)
        return ans
    

reward1 = [1,1,3,4]
reward2 = [4,4,1,1]
reward1 = [99,100]
reward2 = [2,98]
k = 1
sol = Solution()
print(sol.miceAndCheese(reward1, reward2, k))
