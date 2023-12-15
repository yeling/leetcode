
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
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        ans = [0,0]
        arr = [a,b,c]
        arr.sort()
        a,b,c = arr
        if a + 1 == b and b + 1 == c:
            ans[0] = 0
        elif a + 1 == b and b + 1 < c or a + 1 < b and b + 1 == c:
            ans[0] = 1
        elif a + 2 == b or b + 2 == c:
            ans[0] = 1
        else:
            ans[0] = 2

        ans[1] = arr[1] - 1- arr[0] +  arr[2] - 1 - arr[1]
        return ans
    

sol = Solution()
a = 1
b = 3
c = 5
print(sol.numMovesStones(a,b,c))
