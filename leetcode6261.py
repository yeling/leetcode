
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
    def maximumValue(self, strs: List[str]) -> int:
        ans = -1
        for v in strs:
            if v.isdigit():
                ans = max(ans, int(v))
            else:
                ans = max(ans,len(v))
        return ans
    
strs = ["alic3","bob","31","4","00000"]
sol = Solution()
print(sol.maximumValue(strs))
