
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
    # 45 / 47 个通过测试用例
    def isPossible2(self, n: int, edges: List[List[int]]) -> bool:
        g = [list() for _ in range(n + 1)]
        for v in edges:
            g[v[0]].append(v[1])
            g[v[1]].append(v[0])
        # print(g)
        odd = []
        for i,v in enumerate(g):
            if len(v)%2 == 1:
                odd.append(i)
        if len(odd) == 0:
            return True
        elif len(odd) == 2:
            if odd[0] not in g[odd[1]]:
                return True
            else:
                #找公共节点
                cache1 = set(g[odd[0]])
                cache2 = set(g[odd[1]])
                for i in range(1, n + 1):
                    if i not in cache1 and i not in cache2:
                        return True
                return False
        elif len(odd) == 4:
            if odd[0] not in g[odd[1]] and  odd[2] not in g[odd[3]]:
                return True
            elif odd[0] not in g[odd[2]] and  odd[1] not in g[odd[3]]:
                return True
            elif odd[0] not in g[odd[3]] and  odd[1] not in g[odd[2]]:
                return True
            else:
                return False
        else:
            return False

    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        return 
    

n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
# n = 4
# edges = [[1,2],[3,4]]

# n = 4
# edges = [[1,2],[1,3],[1,4]]

n = 21
edges = [[2,19],[16,17],[8,14],[2,16],[12,20],[12,14],[16,18],[15,16],[10,21],[3,5],[13,18],[17,20],[14,17],[9,12],[5,15],[5,6],[3,7],[2,21],[10,13],[8,16],[7,18],[4,6],[9,1],[13,21],[18,20],[7,14],[4,19],[5,8],[3,11],[11,1],[7,12],[4,7],[3,16],[13,17],[17,19],[9,13],[7,19],[10,16],[4,13],[4,5],[2,15],[12,19],[11,16],[2,9],[11,17],[17,1],[16,21],[4,10],[10,14],[14,16],[4,1],[13,20],[5,20],[4,14],[4,21],[10,20],[2,14],[8,15],[4,8],[6,19],[15,1],[19,1],[8,19],[15,21],[3,12],[11,18],[9,17],[18,19],[7,21],[3,21],[16,19],[11,15],[5,1],[8,17],[3,15],[8,1],[10,19],[3,8],[6,16],[2,8],[5,18],[11,13],[11,20],[14,21],[6,20],[4,20],[12,13],[5,12],[10,11],[9,15],[3,19],[9,20],[14,18],[21,1],[13,19],[8,21],[2,13],[3,10],[9,18],[19,21],[6,7],[3,18],[2,18],[6,14],[3,17],[5,21],[14,20],[8,9],[16,1],[3,4],[13,1],[5,9],[4,15],[17,21],[20,21],[2,17],[13,14],[11,14],[9,16],[10,18],[6,15],[6,12],[3,13],[5,11],[6,1],[12,17],[8,10],[5,10],[8,18],[4,12],[10,1],[6,13],[4,18],[7,20],[7,16],[2,6],[12,21],[4,17],[15,18],[13,16],[15,20],[7,10],[6,10],[2,20],[7,15],[18,1],[12,1],[3,20],[7,1],[14,15],[4,9],[11,19],[7,9],[5,17],[18,21],[6,21],[8,11],[6,17],[3,14],[7,11],[5,7],[7,13],[6,8],[6,9],[10,12],[5,16],[2,4],[17,18],[9,11],[12,16],[3,6],[12,18],[3,9],[11,12],[14,19],[10,15],[5,13],[8,13],[15,17],[2,10],[11,21],[20,1],[6,18],[2,12],[19,20],[6,11],[8,12],[2,3],[12,15],[2,11],[9,10],[7,17],[9,19],[13,15],[7,8],[4,11],[2,5],[5,19],[16,20],[15,19],[9,14],[14,1],[10,17],[9,21],[2,7],[8,20],[5,14],[4,16]]

sol = Solution()
print(sol.isPossible2(n,edges))
