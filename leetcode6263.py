
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
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        ans = stones[1] - stones[0]
        for i in range(0, n - 2):
            ans = max(ans, stones[i+2] - stones[i])
        return ans


stones = [0, 3, 9]
sol = Solution()
print(sol.maxJump(stones))
