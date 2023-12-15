
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
    def getFolderNames(self, names: List[str]) -> List[str]:
        cache = set()
        indexCache = defaultdict(int)
        ans = []
        for v in names:
            if v in cache:
                indexCache[v] += 1
                temp = v + '(' + str(indexCache[v]) + ')'
                while temp in cache:
                    indexCache[v] += 1
                    temp = v + '(' + str(indexCache[v]) + ')'
                cache.add(temp)
                ans.append(temp)
            else:
                ans.append(v)
                cache.add(v)

        return ans
    
names = ["gta","gta(1)","gta","avalon"]
names = ["kaido","kaido(1)","kaido","kaido(1)"]
sol = Solution()
print(sol.getFolderNames(names))

