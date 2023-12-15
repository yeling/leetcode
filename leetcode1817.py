
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
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k

        cache = defaultdict(set)
        for id,t in logs:
            cache[id].add(t)
        for v in cache:
            ans[len(cache[v]) - 1] += 1
        return ans
    
logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
logs = [[1,1],[2,2],[2,3]]
k = 4
sol = Solution()
print(sol.findingUsersActiveMinutes(logs, k))
