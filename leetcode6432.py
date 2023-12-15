
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


#查找father
def find(father, u):
    if father[u] != u:
        father[u] = find(father,father[u])
    return father[u]
#合并
def join(father, u, v):
    fu = find(father,u)
    fv = find(father,v)
    if fu != fv:
        father[fu] = fv
        
class Solution:
    
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:    
        
        father = list(range(n))
        for u,v in edges:
            join(father, u, v)
        g = [[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        rootMap = defaultdict(list)
        for i in range(len(father)):
            fa = find(father, father[i])
            temp = rootMap[fa]
            if len(temp) == 0:
                temp.append(0)
                temp.append(0)
            temp[0] += 1
            temp[1] += len(g[i])
        print(rootMap)
        ans = 0
        for k in rootMap:
            temp = rootMap[k]
            if temp[1] == temp[0] * (temp[0] - 1):
                ans += 1
        return ans
    
n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
sol = Solution()
print(sol.countCompleteComponents(n, edges))
