
# auther yeling
from typing import List
from bisect import *
from collections import *


#928. 尽量减少恶意软件的传播 II
#并查集，计算每个节点的最大感染数量
#深度搜索

MOD = 10 ** 9 + 7

class Solution:
    # 29 / 46 
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
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
                
        n = len(graph)
        initial.sort()
        mc = n + 1
        res = -1
        tempS = 0
        for v in initial:
            #每次删除v
            father = [i for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != v and j != v and graph[i][j] == 1:
                        join(father, i, j)
                
            rootMap = defaultdict(int)
            for i  in range(len(father)):
                fa = find(father, father[i])
                rootMap[fa] += 1
            tempS = 0
            allfa = set()
            for k in initial:
                fa = find(father, father[k])
                if k != v and fa not in allfa:
                    allfa.add(fa)
                    tempS += rootMap[fa]
            if tempS < mc:
                mc = tempS
                res = v
            # print(v, tempS)
        
        return res
    
sol = Solution()
graph = [[1,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0],[0,0,1,0,1,0,1,0,0],[0,0,0,1,0,0,0,0,0],[0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1]]
# for v in graph:
#     print(v)
initial = [6,0,4]
# graph = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.minMalwareSpread(graph, initial))
