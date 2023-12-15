
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

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    # 128 / 2144 个通过测试用例
    # 2141 / 2144 个通过测试用例

    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cache = defaultdict(int)
        ans = [0] * 5
        for x,y in coordinates:
            if x - 1 >= 0 and y - 1 >= 0 and x < m and y < n:
                cache[(x-1, y - 1)] += 1
            if y - 1 >= 0 and x + 1 < m and y < n:
                cache[(x, y - 1)] += 1
            if x - 1 >= 0 and x < m and y + 1 < n:
                cache[(x - 1, y)] += 1
            if y + 1 < n and x + 1 < m:
                cache[(x,y)] += 1  
        # print(cache)
        for k in cache:
            ans[cache[k]] += 1
        ans[0] = (m - 1)*(n - 1) - sum(ans)

        return ans
    
m = 3
n = 3
coordinates = [[0,0],[1,1],[0,2]]

# m = 3
# n = 3
# coordinates = [[0,0]]

m = 22
n = 73
coordinates = [[11,14],[16,11],[20,5],[5,33],[14,7],[16,60],[0,15],[15,72],[6,60],[9,16],[14,51],[1,52],[18,24],[17,30],[3,4],[19,13],[9,10],[11,40],[15,7],[13,62],[8,41],[12,71],[4,72],[18,7],[1,0],[4,35],[16,33],[7,30],[13,52],[5,1],[15,21],[3,59],[2,41],[4,28]]

# [1387,122,3,0,0]

sol = Solution()
print(sol.countBlackBlocks(m, n, coordinates))
