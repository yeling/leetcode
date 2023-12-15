
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
    def getMaxFunctionValue2(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        father = list(range(n))
        for i,v in enumerate(receiver):
            join(father, i, v)

        rootMap = defaultdict(list)
        for i in range(len(father)):
            fa = find(father, father[i])
            rootMap[fa].append(i)
        print(rootMap)
        for i in rootMap:
            curr = rootMap[i]
            #自环
            
        return
    
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        self.ans = 0
        self.vis = [False] * n
        def dfs(index, path):
            path.append(index)
            self.vis[index] = True
            if self.vis[receiver[index]] == False:
                dfs(receiver[index], path)
            else:
                if k > len(path):
                    


            return
        
        inList = [[]] * n
        outList = [[]] * n
        for i,v in enumerate(receiver):
            outList[i].append(v)
            inList[v].append(i)
        for i,v in enumerate(receiver):
            if len(inList(i)) == 0 and self.vis[i] == False:
                dfs(i,[])


        return
    
receiver = [2,0,1]
k = 4
sol = Solution()
print(sol.getMaxFunctionValue(receiver,k))
