
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue
from typing import Optional
from heapq import *
import string
# from sortedcontainers import SortedList


INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        grid = [[INF]*26 for _ in range(26)]
        
        for i in range(26):
            grid[i][i] = 0
        for i in range(len(cost)):
            s = ord(original[i]) - ord('a')
            e = ord(changed[i]) - ord('a')
            grid[s][e] = min(grid[s][e],cost[i])
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
        ans = 0
        for i in range(len(source)):
            s = ord(source[i]) - ord('a')
            e = ord(target[i]) - ord('a')
            if grid[s][e] == INF:
                return -1
            else:
                ans += grid[s][e]
        return ans
    
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]

source = "aaaa"
target = "bbbb"
original = ["a","c"]
changed = ["c","b"]
cost = [1,2]

sol = Solution()
print(sol.minimumCost(source, target, original, changed, cost))

