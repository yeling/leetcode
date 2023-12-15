
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
    def countSeniors(self, details: List[str]) -> int:    
        cnt = 0
        for v in details:
            temp = int(v[11:13])
            # print(temp)
            if temp > 60:
                cnt += 1
        return cnt
    
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
sol = Solution()
print(sol.countSeniors(details))
