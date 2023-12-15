
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
    def adventureCamp(self, expeditions: List[str]) -> int:
        cache = set()
        ans = 0
        pos = -1
        n = len(expeditions)
        temp = expeditions[0].split("->")
        for v in temp:
            cache.add(v)
        for i in range(1,n):
            cnt = 0
            temp = expeditions[i].split("->")

            for v in temp:
                if len(v) == 0:
                    continue
                if v not in cache:
                    cnt += 1
                    cache.add(v)
            if cnt > ans:
                ans = cnt
                pos = i

        return pos
    

expeditions = ["leet->code","leet->code","leet->code->leet->courier"]

expeditions = ["Alice->Dex","","Dex"]
sol = Solution()
print(sol.adventureCamp(expeditions))
